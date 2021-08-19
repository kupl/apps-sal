class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sumMax = 0
        nLen1 = len(nums1)
        nLen2 = len(nums2)
        loopLen = min(nLen1, nLen2)

        maxVal = (10**9) + 7

        idx1 = {nums1[0]: 0}
        idx2 = {nums2[0]: 0}
        ps1 = 0
        ps2 = 0
        pe1 = 1
        pe2 = 1
        for i in range(1, loopLen):
            v1 = nums1[i]
            v2 = nums2[i]
            sumT = 0
            if v1 == v2:
                pe1 = i + 1
                pe2 = i + 1
                sum1 = sum(nums1[ps1:pe1])
                sum2 = sum(nums2[ps2:pe2])
                sumT = max(sum1, sum2)
                ps1 = pe1
                ps2 = pe2
            if v1 in idx2:
                pe1 = i + 1
                pe2 = idx2[v1] + 1
                sum1 = sum(nums1[ps1:pe1])
                sum2 = sum(nums2[ps2:pe2])
                sumT = max(sum1, sum2)
                ps1 = pe1
                ps2 = pe2
            elif v2 in idx1:
                pe2 = i + 1
                pe1 = idx1[v2] + 1
                sum1 = sum(nums1[ps1:pe1])
                sum2 = sum(nums2[ps2:pe2])
                sumT = max(sum1, sum2)
                ps1 = pe1
                ps2 = pe2

            # print(i, ps1, pe1, ps2, pe2, sumT)
            sumMax += sumT
            sumMax = sumMax % maxVal

            idx1[v1] = i
            idx2[v2] = i

        if nLen1 > nLen2:
            for i in range(loopLen, nLen1):
                v1 = nums1[i]
                if v1 in idx2:
                    pe1 = i + 1
                    pe2 = idx2[v1] + 1
                    sum1 = sum(nums1[ps1:pe1])
                    sum2 = sum(nums2[ps2:pe2])
                    sumT = max(sum1, sum2)
                    ps1 = pe1
                    ps2 = pe2
                else:
                    sumT = 0
                sumMax += sumT
                sumMax = sumMax % maxVal
                idx1[v1] = i

                if v1 > nums2[-1]:
                    break
        elif nLen2 > nLen1:
            for i in range(loopLen, nLen2):
                v2 = nums2[i]
                if v2 in idx1:
                    pe2 = i + 1
                    pe1 = idx1[v2] + 1
                    sum1 = sum(nums1[ps1:pe1])
                    sum2 = sum(nums2[ps2:pe2])
                    sumT = max(sum1, sum2)
                    ps1 = pe1
                    ps2 = pe2
                else:
                    sumT = 0
                # print(i, ps1, pe1, ps2, pe2, sumT)
                sumMax += sumT
                sumMax = sumMax % maxVal
                idx2[v2] = i

                if v2 > nums1[-1]:
                    break

        # print(ps1, ps2)
        if(ps1 < nLen1):
            sum1 = sum(nums1[ps1:])
        else:
            sum1 = 0

        if(ps2 < nLen2):
            sum2 = sum(nums2[ps2:])
        else:
            sum2 = 0

        sumT = max(sum1, sum2)
        sumMax += sumT
        sumMax = sumMax % maxVal
        return sumMax
