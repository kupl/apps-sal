class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize:
            return 0
        if minSize > maxSize:
            return 0

        res = 0
        d = {}

        for i in range(len(s) - minSize + 1):
            temp = s[i:i + minSize]
            if len(set(temp)) <= maxLetters:
                d[temp] = d.get(temp, 0) + 1
                res = max(res, d[temp])
        return res

        '''
        res=0
        for i in range(minSize,maxSize+1):
            #print(\"a\")
            r=[]
            for j in range(i,len(s)+1):
                #print(s[j-minSize:j])
                a=s[j-minSize:j]
                
                if len(set(list(a)))<=maxLetters:
                #print(set(list(a)))
                    r.append(a)
            #print(r)
            if len(r)!=0:
                r1 = max(set(r), key = r.count) 
            #print(r.count(r1))
                r2=r.count(r1)
                res=max(res,r2)
        return res
        '''
