class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        d = []
        res = 0
        count = 1
        for a in A:
            if (a % 2):
                d.append(count)
                count = 1
            else:
                count += 1
        d.append(count)
        for x, y in zip(d, d[k:]):
            res += x * y
        return res
