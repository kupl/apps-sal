class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return ''
        m = s[0]

        for i in range(1, len(s)):
            m = max(m, s[i])

        x = ''

        for i in range(len(s)):
            if s[i] == m:
                x = max(x, s[i:])
        return x

        '''
        if len(x)==1:
            return s[x[0]:]
        
        
        
        while len(x)>1:
            c=1
            m=s[x[0]+c]
            i=0
            while i<len(x):
                if x[i]+c>=len(s):
                    if len(x)>1:
                        x.pop()
                        break
                    else:
                        return s[x[0]:]
                if s[x[i]+c]<m:
                    del x[i]
                    continue
                if s[x[i]+c]>m:
                    m=s[x[i]+c]
                    x=x[i:]
                    i=0
                    continue
                i+=1
            c+=1
        if x:
            return s[x[0]:]
        
        return ''
        '''
