class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        (g, s) = ([0] * n, [0] * n)
        for i in range(n):
            for j in range(i + 1, n):
                print(rating[j])
                if rating[j] > rating[i]:
                    g[i] += 1
                else:
                    s[i] += 1
        print(g)
        print(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    ans += g[j]
                else:
                    ans += s[j]
        return ans
