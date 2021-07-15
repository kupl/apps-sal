def aux(s,lst,i):
    if(i == len(s)):
        return 0
    mx = 0
    for j in range(i,len(s)):
        #print(lst)
        if(s[i:j+1] not in lst):
            tmp = 1 + aux(s,lst+[s[i:j+1]],j+1)
            if tmp>mx:
                mx = tmp
    return mx

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        lst = []
        return aux(s,lst,0)
