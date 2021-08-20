from collections import deque
from collections import defaultdict


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        mapping = defaultdict(set)
        for (i, val) in enumerate(arr):
            mapping[val].add(i)
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            (curr_cost, ci) = queue.popleft()
            if ci == len(arr) - 1:
                return curr_cost
            if ci + 1 < len(arr) and ci + 1 not in visited:
                queue.append((curr_cost + 1, ci + 1))
                visited.add(ci + 1)
                if ci + 1 in mapping[arr[ci]]:
                    mapping[arr[ci]].remove(ci + 1)
            if ci - 1 >= 0 and ci - 1 not in visited:
                queue.append((curr_cost + 1, ci - 1))
                visited.add(ci - 1)
                if ci - 1 in mapping[arr[ci]]:
                    mapping[arr[ci]].remove(ci - 1)
            next_ = set(mapping[arr[ci]])
            for ni in next_:
                if ni not in visited:
                    queue.append((curr_cost + 1, ni))
                    visited.add(ni)
                mapping[arr[ci]].remove(ni)
        return -1
