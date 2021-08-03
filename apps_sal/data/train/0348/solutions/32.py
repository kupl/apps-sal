class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        r = max(arr)
        if r < 0:
            return r

        l = len(arr)
        f = [0] * l
        b = [0] * l

        cur = 0

        for i in range(l):
            f[i] = cur
            cur += arr[i]
            cur = max(cur, 0)

        cur = 0
        for i in range(l - 1, -1, -1):
            b[i] = cur
            cur += arr[i]
            cur = max(cur, 0)

        return max(f[i] + b[i] for i in range(l))
