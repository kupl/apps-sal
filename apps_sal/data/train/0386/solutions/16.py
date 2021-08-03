from collections import defaultdict


class Solution:

    MOD = 10**9 + 7

    def __init__(self):
        self.cache = defaultdict(dict)

    def countVowelPermutation(self, n: int) -> int:
        return self.count(n)

    def count(self, n: int, vowel: str = None) -> int:
        if n == 0:
            return 1

        if vowel in self.cache[n]:
            return self.cache[n][vowel]

        count = 0
        if vowel == 'a':
            count = self.count(n - 1, 'e')
        elif vowel == 'e':
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'i')
        elif vowel == 'i':
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'e')
            count += self.count(n - 1, 'o')
            count += self.count(n - 1, 'u')
        elif vowel == 'o':
            count = self.count(n - 1, 'i')
            count += self.count(n - 1, 'u')
        elif vowel == 'u':
            count = self.count(n - 1, 'a')
        elif vowel is None:
            count = self.count(n - 1, 'a')
            count += self.count(n - 1, 'e')
            count += self.count(n - 1, 'i')
            count += self.count(n - 1, 'o')
            count += self.count(n - 1, 'u')
        count %= self.MOD
        self.cache[n][vowel] = count
        return count
