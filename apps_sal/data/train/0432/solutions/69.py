import heapq
import collections


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        nums.sort()
        m = collections.defaultdict(list)
        for num in nums:
            left = m.get(num - 1)
            right = m.get(num + 1)
            if left and m[num - 1][0] < k:
                curr = heapq.heappop(m[num - 1])
                heapq.heappush(m[num], curr + 1)
            elif right and m[num + 1][0] < k:
                curr = heapq.heappop(m[num + 1])
                heapq.heappush(m[num + 1], curr + 1)
            else:
                heapq.heappush(m[num], 1)
        for x in m:
            for i in m[x]:
                if i != k:
                    return False
        return True
