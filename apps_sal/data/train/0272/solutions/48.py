class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def dfs(i):
            if i in visited:
                return
            if status[i] == 0:
                missedKey.add(i)
                return
            visited.add(i)
            self.ans += candies[i]

            for k in keys[i]:
                status[k] = 1
                if k in missedKey:
                    missedKey.discard(k)
                    dfs(k)
            for j in containedBoxes[i]:
                dfs(j)

        visited = set()
        missedKey = set()
        self.ans = 0
        for i in initialBoxes:
            dfs(i)

        return self.ans
