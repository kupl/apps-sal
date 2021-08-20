class Solution:

    def countVowelPermutation(self, n: int) -> int:
        f = [[0 for _ in range(5)] for _ in range(n + 1)]
        for i in range(5):
            f[1][i] = 1
        index = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        letter = ['a', 'e', 'i', 'o', 'u']
        pre = {'a': ['e', 'i', 'u'], 'e': ['a', 'i'], 'i': ['e', 'o'], 'o': ['i'], 'u': ['i', 'o']}
        for i in range(2, n + 1):
            for j in range(5):
                tmp = 0
                for k in pre[letter[j]]:
                    tmp += f[i - 1][index[k]]
                f[i][j] = tmp
        return sum(f[n]) % (10 ** 9 + 7)
