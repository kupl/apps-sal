class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        current = 0
        queue = []
        for i in range(len(arr)):
            current += arr[i]
            prefix[current] = i
            if not prefix.get(current - target) is None:
                if len(queue) == 0 or prefix[current - target] + 1 > queue[-1][0]:
                    queue.append((prefix[current - target] + 1, i))
        if len(queue) < 2:
            return -1
        min_q = []
        current = len(arr)
        for i in range(len(queue) - 1, -1, -1):
            current = min(current, queue[i][1] - queue[i][0] + 1)
            min_q.append(current)
        min_q = min_q[::-1]
        pointer1 = 0
        pointer2 = 1
        res = -1
        while pointer2 < len(queue):
            if queue[pointer2][0] <= queue[pointer1][1]:
                pointer2 += 1
                continue
            if res < 0:
                res = queue[pointer1][1] - queue[pointer1][0] + 1 + min_q[pointer2]
            else:
                res = min(res, queue[pointer1][1] - queue[pointer1][0] + 1 + min_q[pointer2])
            pointer1 += 1
        return res
