class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels_idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        f = [None] * n
        # We can safely assume a string can end in any vowel
        f[n - 1] = [1] * len(vowels_idx)
        for i in range(n - 2, -1, -1):
            f[i] = [0] * len(vowels_idx)
            for vowel in vowels_idx:
                # If we have some vowel at current index i, then we know it can only
                # be followed by a specific set of vowels, depending on the vowel at i
                if vowel == 'a':
                    f[i][vowels_idx[vowel]] += f[i + 1][vowels_idx['e']]
                elif vowel == 'e':
                    f[i][vowels_idx[vowel]] += f[i + 1][vowels_idx['a']] + f[i + 1][vowels_idx['i']]
                elif vowel == 'i':
                    f[i][vowels_idx[vowel]] += f[i + 1][vowels_idx['a']] + f[i + 1][vowels_idx['e']] + f[i + 1][vowels_idx['o']] + f[i + 1][vowels_idx['u']]
                elif vowel == 'o':
                    f[i][vowels_idx[vowel]] += f[i + 1][vowels_idx['i']] + f[i + 1][vowels_idx['u']]
                else:
                    f[i][vowels_idx[vowel]] += f[i + 1][vowels_idx['a']]
                f[i][vowels_idx[vowel]] %= (10**9 + 7)
        total = 0
        for vowel in vowels_idx:
            total += f[0][vowels_idx[vowel]]
        return total % (10**9 + 7)

        memo = {}

        def f(i, prev_vowel):
            if i == n:
                return 1

            if (i, prev_vowel) in memo:
                return memo[(i, prev_vowel)]

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

            memo[(i, prev_vowel)] = cnt % (10**9 + 7)
            return cnt

        cnt = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            cnt += f(1, vowel)

        return cnt % (10**9 + 7)
