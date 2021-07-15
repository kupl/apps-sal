class Solution:
    def numTeams(self, rating: List[int]) -> int:
        self.res = 0
        for i in range(len(rating)):
            self.dfs_increase([rating[i]], rating[i+1:], 1)
            self.dfs_decrease([rating[i]], rating[i+1:], 1)
        return self.res
    
    def dfs_increase(self, stack, rating, count):
        if len(stack) == 3:
            self.res += 1
            return
        for i in range(len(rating)):
            if rating[i] > stack[-1]:
                self.dfs_increase(stack + [rating[i]], rating[i+1:], count + 1)
    
    def dfs_decrease(self, stack, rating, count):
        if len(stack) == 3:
            self.res += 1
            return
        for i in range(len(rating)):
            if rating[i] < stack[-1]:
                self.dfs_decrease(stack + [rating[i]], rating[i+1:], count + 1)

