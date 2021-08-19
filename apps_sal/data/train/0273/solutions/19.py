import bisect


class Solution:

    def racecar(self, target: int) -> int:
        speed = 1
        dis = [0]
        while dis[-1] < target:
            dis.append(dis[-1] + speed)
            speed *= 2
        num_moves = self.recur(target, dis, {})
        return num_moves

    def recur(self, target: int, dis: list, memo: dict) -> int:
        if target in memo:
            return memo[target]
        if target in dis:
            return dis.index(target)
        index = bisect.bisect_left(dis, target) - 1
        moves_right = self.recur(dis[index + 1] - target, dis, memo) + 2 + index
        moves_left = self.recur(target - dis[index], dis, memo) + 2 + index
        for i in range(1, index):
            new_moves_left = index + 1 + i + 1 + self.recur(target - dis[index] + dis[i], dis, memo)
            moves_left = min(moves_left, new_moves_left)
        memo[target] = min(moves_right, moves_left)
        return min(moves_right, moves_left)
