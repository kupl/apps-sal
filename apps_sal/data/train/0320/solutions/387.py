class Solution:

    def minOperations(self, nums: List[int]) -> int:
        num_operations = 0
        stacks = [[], []]
        cur_idx = 0
        nxt_idx = 1
        odd = False
        for num in nums:
            if num % 2:
                odd = True
            if num:
                stacks[0].append(num)
        num_operations = 0
        while stacks[0] or stacks[1]:
            if odd:
                while stacks[cur_idx]:
                    nxt = stacks[cur_idx].pop()
                    if nxt % 2:
                        nxt -= 1
                        num_operations += 1
                    if nxt:
                        stacks[nxt_idx].append(nxt)
                odd = False
            else:
                num_operations += 1
                while stacks[cur_idx]:
                    nxt = stacks[cur_idx].pop()
                    nxt /= 2
                    if nxt % 2:
                        odd = True
                    if nxt:
                        stacks[nxt_idx].append(nxt)
            (cur_idx, nxt_idx) = (nxt_idx, cur_idx)
        return num_operations
