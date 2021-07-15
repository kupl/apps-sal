class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        low, high = 1, 10 ** 9
        answer = 0
        while low <= high:
            mid = (low + high) >> 1
            cnt = 0
            temp = -(10 ** 9)
            for i in position:
                if i - temp >= mid:
                    cnt += 1
                    temp = i
            if cnt >= m:
                answer = max(answer, mid)
                low = mid + 1
            else:
                high = mid - 1
        return answer

