import heapq


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        waiting = {}
        nums.sort()
        for num in nums:
            if num not in waiting:
                if num + 1 in waiting:
                    heapq.heappush(waiting[num + 1], k - 1)
                else:
                    waiting[num + 1] = [k - 1]
            else:
                remain = heapq.heappop(waiting[num])
                if len(waiting[num]) == 0:
                    del waiting[num]
                if remain != 1:
                    if num + 1 in waiting:
                        heapq.heappush(waiting[num + 1], remain - 1)
                    else:
                        waiting[num + 1] = [remain - 1]
        for k, v in list(waiting.items()):
            if len(v) > 0:
                return False
        return True
