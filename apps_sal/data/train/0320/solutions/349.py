from collections import deque


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = deque([[nums, 0]])
        while stack:
            cur_nums, count = stack.popleft()
            if all([n == 0 or n == 1 for n in cur_nums]):
                return sum(cur_nums) + count

            if all([n % 2 == 0 for n in cur_nums]):
                stack.append([[n // 2 for n in cur_nums], count + 1])
                continue

            tmp = []
            for n in cur_nums:
                if n % 2 == 1:
                    count += 1
                    tmp.append(n - 1)
                else:
                    tmp.append(n)
            stack.append([tmp, count])
