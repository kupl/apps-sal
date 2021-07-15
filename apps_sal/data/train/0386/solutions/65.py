from collections import defaultdict as dt
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        di={'a':1,'e':1,'i':1,'o':1,'u':1}
        for j in range(1,n):
            e={}
            for i in 'aeiou':
                if i=='e':
                    e[i]= di['a']+di['i']
                elif i=='a':
                    e[i]= di['e']
                elif i=='i':
                    e[i]=di['a']+di['e']+di['o']+di['u']
                elif i=='o':
                    e[i]=di['i']+di['u']
                else:
                    e[i]=di['a']
            di=e
        return sum(list(di.values()))%(10**9+7)
