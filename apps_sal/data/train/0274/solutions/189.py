from heapq import heappush, heappop


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_q = []
        max_q = []
        start_index = 0
        cur_longest_len = 0
        for i, number in enumerate(nums):
            heappush(min_q, (number, i))
            heappush(max_q, (-number, i))
            while self.calc_diff(-max_q[0][0], min_q[0][0]) > limit:
                if min_q[0][1] > max_q[0][1]:
                    value, _index = heappop(max_q)
                    q = max_q
                else:
                    value, _index = heappop(min_q)
                    q = min_q
                start_index = max(_index + 1, start_index)
                while q and q[0][1] < start_index:
                    heappop(q)
            cur_longest_len = max(
                cur_longest_len,
                i - start_index + 1
            )
        return cur_longest_len

    def calc_diff(self, a, b):
        return abs(a - b)
