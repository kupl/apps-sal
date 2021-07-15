class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        d = []
        n = len(A)
        res = 0
        count = 1
        for i in range(n):
            if (A[i] % 2):
                d.append(count)
                count = 1
            else:
                count += 1
        d.append(count)
        for x,y in zip(d,d[k:]):
            res += x * y
        return res
