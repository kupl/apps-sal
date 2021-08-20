class Solution:

    def minJumps_tle(self, arr: List[int]) -> int:
        if not arr:
            return 0
        (visited, L, lookup) = (set(), len(arr), collections.defaultdict(list))
        que = collections.deque()
        que.append((0, 0))
        visited.add(0)
        for (k, v) in enumerate(arr):
            lookup[v].append(k)
        while que:
            (c, s) = que.popleft()
            if c == L - 1:
                return s
            if c + 1 not in visited and c + 1 < L:
                visited.add(c + 1)
                que.append((c + 1, s + 1))
            if L > c - 1 >= 0 and c - 1 not in visited:
                visited.add(c - 1)
                que.append((c - 1, s + 1))
            for i in lookup[arr[c]]:
                if i == c:
                    continue
                if i not in visited and 0 <= i < L:
                    visited.add(i)
                    que.append((i, s + 1))
        return -1

    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0
        (visited, L, lookup) = (set(), len(arr), collections.defaultdict(list))
        que = collections.deque()
        que.append(0)
        visited.add(0)
        for (k, v) in enumerate(arr):
            lookup[v].append(k)
        step = 0
        while que:
            size = len(que)
            for i in range(size):
                c = que.popleft()
                if c == L - 1:
                    return step
                if c + 1 not in visited and 0 <= c + 1 < L:
                    visited.add(c + 1)
                    que.append(c + 1)
                if L > c - 1 >= 0 and c - 1 not in visited:
                    visited.add(c - 1)
                    que.append(c - 1)
                for i in lookup[arr[c]]:
                    if i == c:
                        continue
                    if i not in visited and 0 <= i < L:
                        visited.add(i)
                        que.append(i)
                del lookup[arr[c]]
            step += 1
        return -1
