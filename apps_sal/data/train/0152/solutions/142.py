class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 1
        r = (position[-1]-position[0])//(m-1)
        #print(l,r)
        while (l<=r):
            mid = (l+r)//2
            placed = 1
            distance = 0
            start = position[0]
            for i in range(1,len(position)):
                distance = position[i]-start
                if distance >= mid:
                    placed +=1
                    distance = 0
                    start = position[i]
            #print(placed)
            if placed >=m:
                answer = mid #we placed all balls
                l = mid +1
            else:
                r = mid -1
                
        return(answer)
