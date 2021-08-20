class Solution:

    def minDays(self, n: int) -> int:

        def nex(n):
            ans = [n - 1]
            if n % 2 == 0:
                ans.append(n // 2)
            if n % 3 == 0:
                ans.append(n // 3)
            return ans
        step = 0
        states = [n]
        seen = {n}
        while True:
            states = [v for s in states for v in nex(s) if v not in seen]
            for s in states:
                seen.add(s)
            step += 1
            if 0 in seen:
                return step
