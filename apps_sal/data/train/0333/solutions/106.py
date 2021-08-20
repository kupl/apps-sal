from collections import *


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        mapper = defaultdict(set)
        for (i, x) in enumerate(arr):
            mapper[x].add(i)
        end = len(arr) - 1
        queue = deque([(arr[0], 0, 0)])
        vis = set()
        vis.add(0)
        while queue:
            (num, index, count) = queue.popleft()
            if index == end:
                return count
            if num in mapper:
                for y in mapper.pop(num):
                    if y not in vis:
                        queue.append((arr[y], y, count + 1))
                        vis.add(y)
            if index + 1 <= end and index + 1 not in vis:
                queue.append((arr[index + 1], index + 1, count + 1))
                vis.add(index + 1)
            if index - 1 >= 0 and index - 1 not in vis:
                queue.append((arr[index - 1], index - 1, count + 1))
                vis.add(index - 1)
