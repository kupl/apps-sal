class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n= len(position)
        position.sort()
        if m==2:
            return position[-1]- position[0]
        cache={}
        def F(x):
            placed=1
            prev= position[0]
            for i in range(1, n):
                if position[i]- prev>= x:
                    placed+=1
                    prev= position[i]
                if placed== m:
                    return True
            return False
        def get_x():
            l= 1
            r= position[n-1]- position[0]
            while l<=r:
                mid= (l+r)//2
                if mid not in cache:
                    cache[mid]= F(mid)
                c= cache[mid]
                if c:
                    l= mid+1
                    ans= mid
                else:
                    r=mid-1
            return ans
        return (get_x())

