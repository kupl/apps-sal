from heapq import heappush, heappop


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # min_stack = []
        # max_stack = []
        # for i, number in enumerate(nums):
        #     _index = i
        #     while max_stack and number > max_stack[-1][0]:
        #         _, _index = max_stack.pop()
        #     max_stack.append((number, _index))
        #     _index = i
        #     while min_stack and number < min_stack[-1][0]:
        #         _, _index = min_stack.pop()
        #     min_stack.append((number, _index))
        # longest = -1
        # start_index = len(nums) - 1
        # print(max_stack)
        # print(min_stack)
        # while max_stack[-1][0] - min_stack[-1][0] <= limit:
        #     longest = max(
        #         longest,
        #         abs(max_stack[-1][1] - min_stack[-1][1])
        #     )
        #     if max_stack[-1][1] > min_stack[-1][1]:
        #         max_stack.pop()
        #     else:
        #         min_stack.pop()
        # return longest

        min_q = []
        max_q = []
        start_index = 0
        cur_longest_len = 0
        for i, number in enumerate(nums):
            heappush(min_q, (number, i))
            heappush(max_q, (-number, i))
            while self.calc_diff(-max_q[0][0], min_q[0][0]) > limit:
                # print(self.calc_diff(-max_q[0][0], min_q[0][0]) )
                if min_q[0][1] > max_q[0][1]:
                    value, _index = heappop(max_q)
                    q = max_q
                else:
                    value, _index = heappop(min_q)
                    q = min_q
                start_index = max(_index + 1, start_index)
                # print(start_index, value, q)
                # print(start_index, _index, value)
                while q and q[0][1] < start_index:
                    heappop(q)
            cur_longest_len = max(
                cur_longest_len,
                i - start_index + 1
            )
            # if cur_longest_len == 3:
            #     print(\"HERE\", start_index, i)
        # print(max_q)
        # print(min_q)
        return cur_longest_len

    def calc_diff(self, a, b):
        return abs(a - b)
