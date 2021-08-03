class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        target, stones, memo = stones[-1], set(stones), set()

        return self.dfs(stones, 1, 1, target, memo)

    def dfs(self, stones, pos, jump, target, memo):
        if (pos, jump) in memo:
            return False
        if pos == target:
            return True
        if pos not in stones or jump <= 0:
            return False

        for j in (jump - 1, jump, jump + 1):
            if self.dfs(stones, pos + j, j, target, memo):
                return True
        memo.add((pos, jump))   # record bad position and jump
        return False
