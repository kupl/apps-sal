class Solution:
    from collections import deque
    def minDays(self, n: int) -> int:
        
        q=deque()
        q.append(n)
        seen=set()
        ans=1
        
        while q:
            
            new=deque()
            
            while q:
                k=q.popleft()

                if k==1:
                    return ans
                seen.add(k)


                if k%3==0 and k//3 not in seen:
                    new.append(k//3)
                if k%2==0 and k//2 not in seen:
                    new.append(k//2)
                if k-1 not in seen:
                    new.append(k-1)
            
            q=new
            
            ans+=1

