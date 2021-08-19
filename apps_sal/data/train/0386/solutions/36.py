class Solution:

    def countVowelPermutation(self, n: int) -> int:
        memo = dict()

        def helper(char: str, x: int):
            if (char, x) in memo:
                return memo[char, x]
            if x == 1:
                memo[char, x] = 1
                return memo[char, x]
            if char == 'a':
                memo[char, x] = helper('e', x - 1)
            elif char == 'e':
                memo[char, x] = helper('a', x - 1) + helper('i', x - 1)
            elif char == 'i':
                memo[char, x] = sum((helper(c, x - 1) for c in 'aeou'))
            elif char == 'o':
                memo[char, x] = helper('i', x - 1) + helper('u', x - 1)
            elif char == 'u':
                memo[char, x] = helper('a', x - 1)
            return memo[char, x]
        total = sum((helper(c, n) for c in 'aeiou'))
        return total % (10 ** 9 + 7)
