class Solution:

    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        d = defaultdict(list)
        for (i, val) in enumerate(arr):
            d[val].append(i)
        visited = set([0])
        stack = deque([0])
        (k, jumps) = (len(stack), 1)
        while stack:
            i = stack.popleft()
            childs = [j for j in [i - 1, i + 1] if arr[j] != arr[i]] + [j for j in d.pop(arr[i], [])]
            childs = [j for j in childs if 0 <= j < n and j not in visited]
            for j in childs:
                if j == n - 1:
                    return jumps
                visited.add(j)
                stack.append(j)
            k -= 1
            if not k:
                k = len(stack)
                jumps += 1
        return jumps
