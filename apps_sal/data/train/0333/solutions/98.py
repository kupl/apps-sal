class Solution:

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        pos = defaultdict(list)
        for (i, num) in enumerate(arr):
            pos[num].append(i)
        (q, steps) = (deque([0]), 0)
        seen = [False] * n
        seen[0] = True
        while q:
            size = len(q)
            for _ in range(size):
                i = q.popleft()
                if i == n - 1:
                    return steps
                if i + 1 < n and (not seen[i + 1]):
                    q.append(i + 1)
                    seen[i + 1] = True
                if i - 1 > -1 and (not seen[i - 1]):
                    q.append(i - 1)
                    seen[i - 1] = True
                for j in pos[arr[i]]:
                    if not seen[j]:
                        q.append(j)
                        seen[j] = True
                pos[arr[i]].clear()
            steps += 1
        return -1
