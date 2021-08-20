class Solution:

    def racecar(self, target: int) -> int:

        def dfs(distance):
            if distance in dp:
                return dp[distance]
            (position, speed, counter) = (0, 1, 0)
            res = float('inf')
            arr = [0]
            while position < distance:
                (position, speed, counter) = (position + speed, speed * 2, counter + 1)
                if position < distance:
                    for x in arr:
                        res = min(res, counter + 2 + dfs(distance - position + x) + dp[x])
                else:
                    res = min(res, counter + 1 + dfs(position - distance))
                arr.append(position)
            dp[distance] = res
            return res
        (position, speed, counter) = (0, 1, 0)
        dp = {0: 0}
        while position < target:
            (position, speed, counter) = (position + speed, speed * 2, counter + 1)
            dp[position] = counter
        return dfs(target)
