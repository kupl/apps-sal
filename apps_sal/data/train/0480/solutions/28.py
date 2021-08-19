class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        ans = 0

        mem = [dict() for _ in range(501)]

        def dfs(s, arrLen, pos):
            nonlocal ans
            if pos < 0 or pos >= arrLen:
                return 0

            if s == 0 and pos == 0:
                return 1

            if s < 0:
                return 0

            if pos in mem[s]:
                return mem[s][pos]

            s1 = dfs(s - 1, arrLen, pos)
            s2 = dfs(s - 1, arrLen, pos + 1)
            s3 = dfs(s - 1, arrLen, pos - 1)

            total = (s1 + s2 + s3)

            if not pos in mem[s]:
                mem[s][pos] = total

            #print(s, pos, total)

            return total

        ans = dfs(steps, arrLen, 0)

        return ans % (10**9 + 7)
