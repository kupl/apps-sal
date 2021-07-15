class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        def count(d):
            answer, curr = 1, position[0]
            for i in range(1,n):
                if position[i] - curr >= d:
                    answer+=1
                    curr = position[i]
            return answer
        left, right = 0, position[-1] - position[0]
        while left < right :
            mid = right - (right- left)//2
            if count(mid) >= m :
                left = mid
            else:
                right = mid - 1
        return left
