class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        from collections import defaultdict
        
        end = dict()
        end['a'] = 1
        end['e'] = 1
        end['i'] = 1
        end['o'] = 1
        end['u'] = 1
                        
        for j in range(n-1):
            
            for_a = end['e'] + end['i'] + end['u']
            for_e = end['a'] + end['i']
            for_i = end['e'] + end['o']
            for_o = end['i']
            for_u = end['o'] + end['i']

            end['a'] = for_a
            end['e'] = for_e
            end['i'] = for_i
            end['o'] = for_o
            end['u'] = for_u
                        
        count = sum([v for k, v in end.items()])
        
        return count % (10**9 + 7)      
