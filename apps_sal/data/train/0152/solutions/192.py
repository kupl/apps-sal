from collections import deque

class Solution:
    def helper(self, minforce, position, m):
        #returns if minforce is valid or not
        counter = 1
        prev = position[0]
        i = 1
        while i < len(position) and counter < m:
            if position[i] - prev < minforce:
                i += 1
            else:
                counter += 1
                prev = position[i]
                i += 1
        if counter == m:
            return True
        else:
            return False
    
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left = 1
        right = position[-1] - position[0]
        if m==2:
            return right
        while left < right:
            mid = left + (right - left)//2
            #print(mid)
            if self.helper(mid, position, m):
                left = mid + 1
            else:
                right = mid
        return left-1
