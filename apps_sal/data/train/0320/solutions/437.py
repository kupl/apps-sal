class Solution:
    def minOperations(self, t: List[int]) -> int:
        n = len(t)
        ans = 0
        while (1):
            z = 0
            i = 0
            while (i < n):
                if ((t[i] % 2)):
                    break

                elif (t[i] == 0):
                    z += 1
                i += 1
            if (z == n):
                return ans
            if (i == n):
                for j in range(n):
                    t[j] = t[j] // 2
                ans += 1
            for j in range(i, n):
                if (t[j] & 1):
                    t[j] -= 1
                    ans += 1
        return ans
