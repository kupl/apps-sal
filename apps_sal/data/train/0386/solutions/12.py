class Solution:

    def countVowelPermutation(self, n: int) -> int:
        memo = {}

        def f(i, prev_vowel):
            if i == n:
                return 1
            if (i, prev_vowel) in memo:
                return memo[i, prev_vowel]
            cnt = 0
            if prev_vowel == 'a':
                cnt += f(i + 1, 'e')
            elif prev_vowel == 'e':
                cnt += f(i + 1, 'a') + f(i + 1, 'i')
            elif prev_vowel == 'i':
                cnt += f(i + 1, 'a') + f(i + 1, 'e') + f(i + 1, 'o') + f(i + 1, 'u')
            elif prev_vowel == 'o':
                cnt += f(i + 1, 'i') + f(i + 1, 'u')
            else:
                cnt += f(i + 1, 'a')
            memo[i, prev_vowel] = cnt % (10 ** 9 + 7)
            return cnt
        cnt = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            cnt += f(1, vowel)
        return cnt % (10 ** 9 + 7)
