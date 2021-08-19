class Solution:

    def getProbability(self, balls: List[int]) -> float:
        self.total = 0
        self.valid = 0
        t = sum(balls) >> 1
        n = len(balls)

        def check(s):
            return sum([x != 0 for x in s]) == sum([balls[i] - s[i] != 0 for i in range(n)])
        fac = [1]
        for i in range(1, t + 1):
            fac.append(fac[-1] * i)

        def update(s):
            x = y = fac[-1]
            cnt1 = cnt2 = 0
            for (i, c) in enumerate(s):
                x //= fac[c]
                y //= fac[balls[i] - c]
                cnt1 += c > 0
                cnt2 += balls[i] - c > 0
            ret = x * y
            self.total += ret
            if cnt1 == cnt2:
                self.valid += ret

        def dfs(state, i):
            (s, cnt) = state
            if cnt == t:
                update(s)
                return
            if i == n:
                return
            for x in range(balls[i] + 1):
                if cnt + x > t:
                    break
                s[i] = x
                dfs((s, cnt + x), i + 1)
                s[i] = 0
        s = [0] * n
        dfs((s, 0), 0)
        print(self.valid)
        print(self.total)
        return self.valid / self.total
