class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a={}
        b={}
        for i in s:
            if i in a:
                a[i] +=1
            else:
                a[i] = 1
        for j in t:
            if j in b:
                b[j] +=1
            else:
                b[j] =1
        v=0
        for i in a:
            if i in b and a[i] > b[i]:
                v+=a[i]-b[i]
            elif i not in b:
                v += a[i]
            else:
                v +=0
        return(v)
