class Solution1:

    def __init__(self):
        self.dp = {0: 0}

    def racecar(self, target: int) -> int:
        if target in self.dp:
            return self.dp[target]
        n = target.bit_length()
        if 2 ** n - 1 == target:
            self.dp[target] = n
        else:
            self.dp[target] = self.racecar(2 ** n - 1 - target) + n + 1
            for m in range(n - 1):
                self.dp[target] = min(self.dp[target],
                                      self.racecar(target - 2 ** (n - 1) + 2 ** m) + n + m + 1)

        return self.dp[target]


class Solution2:
    def racecar(self, target: int) -> int:
        memo = [-1] * (target * 2)

        def DP(s):
            if memo[s] > 0:
                return memo[s]
            duishu = math.log2(s + 1)
            if int(duishu) == duishu:
                memo[s] = duishu
                return duishu
            left = int(duishu)
            right = int(duishu) + 1
            memo[s] = right + 1 + DP(2**right - s - 1)
            for i in range(left):
                huizou = 2**i - 1
                memo[s] = min(memo[s], left + i + 2 + DP(s - 2**left + 1 + huizou))
            return memo[s]
        return int(DP(target))


class Solution:
    def racecar(self, target: int) -> int:
        visited = {(0, 1)}
        queue = collections.deque()
        queue.append((0, 1))
        steps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                s, v = queue.popleft()
                if s == target:
                    return steps
                cur_s = s + v
                cur_v = v * 2
                if (cur_s, cur_v) not in visited and s >= 0:
                    queue.append((cur_s, cur_v))
                    visited.add((cur_s, cur_v))
                cur_s = s
                cur_v = -1 if v > 0 else 1
                if (cur_s, cur_v) not in visited and s >= 0:
                    queue.append((cur_s, cur_v))
                    visited.add((cur_s, cur_v))
            steps += 1
