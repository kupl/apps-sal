class Solution:
    
        
    
    def findKthBit(self, n: int, k: int) -> str:
        s=[]
        for i in range(n):
            if i==0:
                s.append(['0'])
            else:
                temp=(s[i-1]).copy()
                for j in range(len(temp)):
                    if temp[j]=='0':
                        temp[j]='1'
                        
                        # temp2=''
                        # temp=(temp2.join(temp)) 
                        
                        
                    else:
                        # temp=list(temp)
                        temp[j]='0'
                        
                        # temp2=''
                        # temp=(temp2.join(temp)) 
                temp=temp[::-1]
                
                s.append([])
                for zz in s[i-1]:
                    s[i].append(zz)
                s[i].append('1')
                for zz in temp:
                    s[i].append(zz)
                
                
        
        # for i in (s[k-1]):
        #     print(i)
        return (s[-1][k-1])
                

