class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        v = []
        n = len(arr)
        for i in range(n):
            v.append((arr[i], i))
        v = sorted(v)

        f = [-1] * n
        ans = -1
        for i in range(n):
            idx = v[i][1]
            f[idx] = 1
            for j in range(1, d + 1):
                if idx - j >= 0 and arr[idx - j] < arr[idx]:
                    f[idx] = max(f[idx], f[idx - j] + 1)
                else:
                    break
            for j in range(1, d + 1):
                if idx + j < n and arr[idx + j] < arr[idx]:
                    f[idx] = max(f[idx], f[idx + j] + 1)
                else:
                    break
            ans = max(ans, f[idx])

        return ans
