class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if(not position):
            return 0
        # def comp(a):
        #     return a[1],a[0]
        arr = list(zip(position,speed))
        arr.sort(reverse=True)
        ans=1
        reach=(target-arr[0][0])/arr[0][1]
        for p,s in arr[1:]:
            curr = (target-p)/s
            if(curr>reach):
                ans+=1
                reach=curr
        return ans
            
            
            
            
        

