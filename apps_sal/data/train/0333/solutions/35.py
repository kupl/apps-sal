class Solution:

    def minJumps(self, arr: List[int]) -> int:
        print(len(arr))
        adj = collections.defaultdict(list)
        for (i, n) in enumerate(arr):
            adj[n].append(i)
        q = collections.deque()
        q.append((0, 0))
        used = [False] * len(arr)
        i = 0
        while q:
            (cur, step) = q.popleft()
            print(len(q))
            if cur == len(arr) - 1:
                return step
            if cur < len(arr) - 1 and (not used[cur + 1]):
                used[cur + 1] = True
                q.append((cur + 1, step + 1))
            if cur > 0 and (not used[cur - 1]):
                used[cur - 1] = True
                q.append((cur - 1, step + 1))
            for nxt in adj[arr[cur]]:
                if not used[nxt]:
                    used[nxt] = True
                    q.append((nxt, step + 1))
            adj[arr[cur]] = [k for k in adj[arr[cur]] if not used[nxt]]
        return -1
