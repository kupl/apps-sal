import queue
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n%k != 0:
            return False
        dic = collections.defaultdict(list)
        nums = sorted(nums)
        for i, num in enumerate(nums):
            cur_length = heapq.heappop(dic[num-1]) if dic[num-1] and dic[num-1][0]!=k else 0
            heappush(dic[num],cur_length+1)

        for key in dic:
            for x in dic[key]:
                if x != k:
                    return False
        return True

