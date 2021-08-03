class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''res=0
        for i in range(len(seats)):
            if seats[i]==1:
                continue
            if sum(seats[:i])==0:
                left=0
            else:
                left=i-1
                while seats[left]!=1:
                    left-=1
            if sum(seats[i+1:])==0:
                right=len(seats)-1
            else:
                right=i+1                
                while seats[right]!=1:
                    right+=1
            if i-left!=0 and right-i!=0:
                res=max(res,min(i-left,right-i))
            if i-left==0:
                res=max(res,right-i)
            if right-i==0:
                res=max(res,i-left)

        return(res)'''
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
