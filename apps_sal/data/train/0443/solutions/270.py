class Solution:
    def solve_inc(self, rating, count, idx, last):
        if(count == 3):
            return 1
        if(idx >= len(rating)):
            return 0
        if(rating[idx] > last):
            return self.solve_inc(rating, count + 1, idx + 1, rating[idx]) + self.solve_inc(rating, count, idx + 1, last)
        else:
            return self.solve_inc(rating, count, idx + 1, last)

    def solve_dec(self, rating, count, idx, last):
        if(count == 3):
            return 1
        if(idx >= len(rating)):
            return 0
        if(rating[idx] < last):
            return self.solve_dec(rating, count + 1, idx + 1, rating[idx]) + self.solve_dec(rating, count, idx + 1, last)
        else:
            return self.solve_dec(rating, count, idx + 1, last)

    def numTeams(self, rating: List[int]) -> int:
        idx = 0
        res = 0
        for i in range(len(rating)):
            res += self.solve_inc(rating, 1, i + 1, rating[i])
            res += self.solve_dec(rating, 1, i + 1, rating[i])
        return res
