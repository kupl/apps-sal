from collections import Counter


class Solution:

    def maxEqualFreq(self, nums: List[int]) -> int:
        val_occurences = Counter(nums)
        occ_count = Counter([v for (k, v) in list(val_occurences.items())])
        M = len(nums)
        for i in range(M - 1, -1, -1):
            if len(occ_count) == 2:
                for (k, v) in list(occ_count.items()):
                    if v == 1 and (k - 1 in occ_count or k - 1 == 0):
                        return i + 1
            elif len(occ_count) == 1:
                if 1 in list(occ_count.keys()) or 1 in list(occ_count.values()):
                    return i + 1
            val = nums[i]
            count = val_occurences[val]
            val_occurences[val] -= 1
            if val_occurences[val] == 0:
                del val_occurences[val]
            occ_count[count] -= 1
            if occ_count[count] == 0:
                del occ_count[count]
            if count - 1 != 0:
                occ_count[count - 1] += 1
        return 0
