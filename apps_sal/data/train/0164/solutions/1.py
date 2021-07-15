class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n=len(num)
        if k<=0:
            return num
        
        if k>n*(n-1)//2:
            return ''.join(sorted(list(num)))
        
        for i in range(10):
            idx = num.find(str(i))
            if idx>=0 and idx<=k:
                return num[idx]+self.minInteger(num[:idx]+num[idx+1:],k-idx)
        
        
        
        
        
        
        '''from collections import deque
        j=0
        
        arr=[deque() for i in range(10)]
        
        n=len(num)
        
        for i in range(n):
            arr[int(num[i])].append(i)
            #print(arr)
        
        curr=0
        ans=\"\"
        
        def fun(x,y):
            l=list(arr[x])
            l.append(y)
            l.sort()
            arr[x]=deque(l)
        
        while k>0 and curr<n:
            ch=None
            ch_ind=curr
            for i in range(0,int(num[curr])):
                if arr[i] and arr[i][0]<=k:
                    ch=i
                    ch_ind=arr[i][0]
                    arr[i].popleft()
                    break
                    
            print(arr,ch,ch_ind,curr,k)
            if ch:
                ans+=str(ch)
                k-=(ch_ind-curr)
                
            else:
                ans+=num[curr]
                curr+=1
            print(ans)
            
        
        return ans'''
