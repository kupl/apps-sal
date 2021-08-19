class Solution:

    def racecar(self, target: int) -> int:
        states = set([(0, 1)])
        que = collections.deque([[0, 1]])
        cost = 0
        while que:
            for _ in range(len(que)):
                (pos, speed) = que.popleft()
                if pos == target:
                    return cost
                if pos < 0 or pos >= 2 * target:
                    continue
                for (npos, nspeed) in [[pos, 1 if speed < 0 else -1], [pos + speed, speed * 2]]:
                    if (npos, nspeed) not in states:
                        states.add((npos, nspeed))
                        que.append([npos, nspeed])
            cost += 1
        return -1
    dp = {0: 0}

    def racecar_DP(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if (1 << n) - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2 ** n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[t]
