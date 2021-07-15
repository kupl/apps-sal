class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dic = {}
        dic['a'] = 1
        dic['e'] = 1
        dic['i'] = 1
        dic['o'] = 1
        dic['u'] = 1
                        
        for j in range(n-1):
            
            counta = dic['e']
            counte = dic['a'] + dic['i']
            counti = dic['e'] + dic['o'] + dic['a'] + dic['u']
            counto = dic['i'] + dic['u']
            countu = dic['a']

            dic['a'] = counta
            dic['e'] = counte
            dic['i'] = counti
            dic['o'] = counto
            dic['u'] = countu
                        
        count = sum([v for k, v in dic.items()])
        
        return count % (10**9 + 7)
