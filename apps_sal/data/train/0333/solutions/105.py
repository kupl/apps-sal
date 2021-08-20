from collections import defaultdict, deque


class Solution:

    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        mapping = defaultdict(list)
        for (idx, val) in enumerate(arr):
            mapping[val].append(idx)
        visited = set()
        que = deque()
        que.append((0, 0))
        visited.add(0)
        m = len(arr)
        while que:
            top = que.popleft()
            (idx, depth) = (top[0], top[1])
            if idx + 1 < m and idx + 1 not in visited:
                if idx + 1 == m - 1:
                    return depth + 1
                visited.add(idx + 1)
                que.append((idx + 1, depth + 1))
            if idx - 1 >= 0 and idx - 1 not in visited:
                visited.add(idx - 1)
                que.append((idx - 1, depth + 1))
            for neigh in mapping[arr[idx]]:
                if neigh not in visited:
                    if neigh == m - 1:
                        return depth + 1
                    visited.add(neigh)
                    que.append((neigh, depth + 1))
            mapping.pop(arr[idx])
        return -1
