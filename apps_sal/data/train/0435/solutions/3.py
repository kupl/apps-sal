class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        countPrefs = {0: 1}
        total = 0
        res = 0
        for i, num in enumerate(A):
            total += num
            res += countPrefs.get(total % K , 0)
            if total % K in countPrefs:
                countPrefs[total % K] += 1
            else:
                countPrefs[total % K] = 1
        return res

