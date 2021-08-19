class Solution:

    def countVowelPermutation(self, n: int) -> int:
        """

        """
        g = {'a': ['e'], 'e': ['a', 'i'], 'i': ['a', 'e', 'o', 'u'], 'o': ['i', 'u'], 'u': ['a']}
        d2i = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        newg = {}
        for (k, v) in g.items():
            newg[d2i[k]] = [d2i[letter] for letter in v]
        mod = 10 ** 9 + 7
        prev = [1] * 5
        for _ in range(n - 1):
            dp = [None] * 5
            for i in range(5):
                dp[i] = sum((prev[j] for j in newg[i])) % mod
            prev = dp
        return sum(prev) % mod
