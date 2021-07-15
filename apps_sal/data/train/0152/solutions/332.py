class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def c(p,m,d):
            b=m-1
            l=len(p)
            acc=0
            for i in range(1,l):
                acc+=p[i]-p[i-1]
                if acc>=d:
                    acc=0
                    b-=1
                if b==0:
                    return True
            return False
        low=1
        high=1000000000
        mid=0
        position.sort()
        while low<=high:
            mid=(low+high)//2
            if c(position,m,mid):
                low=mid+1
            else:
                high=mid-1
        return high
