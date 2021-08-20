class Solution:

    def my_function(self, start: int, end: int) -> int:
        if end - start <= 1:
            return 0
        s = sorted(range(end - start), key=lambda x: self.rating[start + x])
        return abs(s.index(0) - s.index(end - start - 1)) - 1

    def numTeams(self, rating: List[int]) -> int:
        self.rating = rating
        total = 0
        l = len(rating)
        for i in range(l):
            for j in range(l - i - 1):
                a = self.my_function(i, l - j)
                total += a
        return total
