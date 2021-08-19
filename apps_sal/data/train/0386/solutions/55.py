class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for _ in range(n - 1):
            a = dic['e'] + dic['i'] + dic['u']
            e = dic['a'] + dic['i']
            i = dic['e'] + dic['o']
            o = dic['i']
            u = dic['o'] + dic['i']
            dic['a'] = a
            dic['e'] = e
            dic['i'] = i
            dic['o'] = o
            dic['u'] = u
        count = 0
        for value in list(dic.values()):
            count += value
        return count % (10 ** 9 + 7)
