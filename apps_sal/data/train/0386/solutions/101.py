class Solution:
    def countVowelPermutation(self, n: int) -> int:
        valid = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a',
        }

        cmap = {
            'a': 0,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4,
        }

        last = [1] * 5
        for i in range(n - 1):
            nex = [0] * 5
            for j in 'aeiou':
                for k in valid[j]:
                    # nex[cmap[k]] += last[cmap[j]] % (10**9+7)
                    nex[cmap[k]] += last[cmap[j]]
            last = nex
        return sum(last) % (10**9 + 7)
