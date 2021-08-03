class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            s1 = Counter(nums1)
            s2 = Counter(nums2)
            cnt = 0
            for i in range(len(nums1)):
                need = nums1[i] * nums1[i]
                if need == 0:
                    if 0 in s2:
                        cnt += s2[0] * (len(num2) - 1) - (s2[0] - 1) * (s2[0] - 1)
                    else:
                        cnt += 0
                else:
                    for j in range(len(nums2)):
                        kk = need / nums2[j]
                        if kk in s2:
                            if nums2[j] != kk:
                                cnt += s2[kk] / 2
                            else:
                                cnt += (s2[kk] - 1) / 2

            return int(cnt)
        return helper(nums1, nums2) + helper(nums2, nums1)
