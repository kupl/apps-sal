class Solution:

    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        suma = [0] * (n + 1)
        for i in range(1, n + 1):
            suma[i] = suma[i - 1] + A[i - 1]
        left = 0
        res = 0
        m = collections.defaultdict(lambda: 0)
        m[0] = 1
        for i in range(n):
            if suma[i + 1] - S in m:
                res += m[suma[i + 1] - S]
            m[suma[i + 1]] += 1
        return res
