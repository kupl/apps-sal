class Solution:
    def f(self, s):    
        xss = []
        if len(s) == 0:
            temp = []
            temp.append('')
            xss.append(temp)
            return xss
        for i in range(1,len(s)+1):
            xs = self.f(s[i:])
            for x in xs:
                if s[:i] not in x:
                    x.append(s[:i])
                    xss.append(x)
  
        return xss
                
    def maxUniqueSplit(self, s: str) -> int:
        x = max([len(y) for y in self.f(s)])
        
        return x-1
