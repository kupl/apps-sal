from bisect import bisect_left
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # log(D) * log(N) * M
        n = len(position)
        position.sort()
        left, right = 1, (position[-1]-position[0])//(m-1)
        ans = 1
        while left <= right:
            mid = (left+right)//2
            #print(left, right, mid)
            head = 0
            remains = m-1
            while remains > 0:
                target = position[head] + mid
                if target > position[-1]:
                    break
                head = bisect_left(position, target, head)
                remains -= 1
                
            if remains == 0:
                #ans = mid
                left = mid+1
            else:
                right = mid-1
                
        return right
