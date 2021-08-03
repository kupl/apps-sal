from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        d = defaultdict(list)
        for i, val in enumerate(arr):
            d[val].append(i)

        visited = set([0])
        stack = deque([0])
        k, jumps = len(stack), 1
        while stack:
            k -= 1
            i = stack.popleft()
            childs = [j for j in d.pop(arr[i], [])]
            for j in [i - 1, i + 1]:
                if 0 <= j < n and arr[j] != arr[i] and j not in visited:
                    childs.append(j)
            visited |= set(childs)
            if n - 1 in visited:
                return jumps
            stack += childs
            if not k:
                k = len(stack)
                jumps += 1
        return jumps
