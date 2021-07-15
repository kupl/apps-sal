class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def is_possible(gap,left):
            prev=position[0]
            for i in range(1,len(position)):
                if position[i]-prev>=gap:
                    prev=position[i]
                    left-=1
                if not left: return True
            return False
        position.sort()
        l,r,ans=0,position[-1],0
        while l<=r:
            gap=l+(r-l)//2
            if is_possible(gap,m-1):
                ans=gap
                l=gap+1
            else:
                r=gap-1
        return ans
