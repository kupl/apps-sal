class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        r=0
        m=len(s)
        for i in range(2**(m-1)):
            #b='{0:07b}'.format(i)
            bb='{0:0'+str(m-1)+'b}'
            b=bb.format(i)
            #print(b)
            st=0
            l=[]
            for k in range(len(b)):
                if b[k]=='1':
                    #print(st,k+1)
                    if k+1>st:
                        l.append(s[st:k+1])
                    st=k+1
            
            if st<len(b)+1:
                l.append(s[st:len(b)+1])
            #print(l)
            if len(l)==len(set(l)):
                r=max(r,len(l))
        print(r)
        return r
