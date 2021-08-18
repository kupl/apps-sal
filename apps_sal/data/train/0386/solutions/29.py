class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dic = {}
        dic['a'] = ['e']
        dic['e'] = ['a', 'i']
        dic['i'] = ['a', 'e', 'o', 'u']
        dic['o'] = ['i', 'u']
        dic['u'] = ['a']
        vowels = ['a', 'e', 'i', 'o', 'u']
        dp = {}
        for v in vowels:
            dp[(v, 1)] = 1

        for i in range(2, n + 1):
            for v in vowels:
                for followed in dic[v]:
                    dp[(v, i)] = dp.get((v, i), 0) + dp[(followed, i - 1)]
        res = 0
        for v in vowels:
            res += dp[(v, n)]
        return res % (10**9 + 7)
