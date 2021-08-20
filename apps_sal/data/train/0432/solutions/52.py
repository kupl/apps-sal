import queue


class Solution:

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums = sorted(nums)
        if len(nums) % k != 0:
            return False
        arr_list = []
        q = queue.PriorityQueue()
        for (ind, num) in enumerate(nums):
            if not q.qsize() or q.queue[0][0] + 1 != num:
                q.put([num, [num]])
            if q.queue[0][0] + 1 == num:
                (val, tmp_list) = q.get()
                tmp_list.append(num)
                if len(tmp_list) == k:
                    continue
                else:
                    q.put([num, tmp_list])
        return True if not q.qsize() else False
