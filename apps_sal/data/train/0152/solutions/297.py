class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        maxVal = position[-1] - position[0]
        answer = 0

        low, high = 1, maxVal

        def isValid(mid):
            pos = position[0]
            elements = 1
            for i in range(1, len(position)):
                if (position[i] - pos >= mid):
                    pos = position[i]
                    elements += 1
                    if (elements == m):
                        return True
            return False

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                answer = max(answer, mid)
                low = mid + 1
            else:
                high = mid - 1

        return answer
