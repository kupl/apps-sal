class Solution:
    def validTriple(self, a, b, c):
        if (a < b and b < c) or (c < b and b < a):
            return True
        return False

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                for k in range(j + 1, len(rating)):
                    if self.validTriple(rating[i], rating[j], rating[k]):
                        ans += 1
        return ans
