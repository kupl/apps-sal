class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def count(nums1, nums2):
            triplets = 0

            cnt2 = {}
            for i2, num2 in enumerate(nums2):
                if num2 not in cnt2:
                    cnt2[num2] = []
                cnt2[num2].append(i2)

            for i1, num1 in enumerate(nums1):
                square = num1 ** 2

                for num2j, idxs2j in cnt2.items():
                    if square % num2j != 0:
                        continue

                    num2k = int(square // num2j)

                    if num2k not in cnt2:
                        continue

                    idxs2k = cnt2[num2k]

                    combined = []
                    for idx2j in idxs2j:
                        combined.append((idx2j, 0))
                    for idx2k in idxs2k:
                        combined.append((idx2k, 1))
                    combined.sort()
                    temp_cnt = 0
                    for comb in combined:
                        idx, ty = comb
                        if ty == 0:
                            triplets += temp_cnt
                        else:
                            temp_cnt += 1

            return triplets

        triplets1 = count(nums1, nums2)
        triplets2 = count(nums2, nums1)

        return triplets1 + triplets2
