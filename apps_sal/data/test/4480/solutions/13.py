class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        d = defaultdict(list)
        sumn = 0
        for i, num in enumerate(A):
            sumn += num
            d[sumn].append(i)

        if sumn % 3 != 0:
            return False
        div = sumn // 3

        return div in d and div * 2 in d and d[div][0] < (d[div * 2][-1] if d[div * 2][-1] != len(A) - 1 else d[div * 2][-2])
