class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dic=collections.defaultdict(list)
        for i ,e in enumerate(s):
            dic[e].append(i)
            
        for k in dic.keys():
            dic[k].append(len(s))
            dic[k].insert(0,-1)
            
        res=0
        for v in dic.values():
            for i in range(1,len(v)-1):
                res+=((v[i]-v[i-1])*(v[i+1]-v[i]))%(10**9+7)
                
        return res
