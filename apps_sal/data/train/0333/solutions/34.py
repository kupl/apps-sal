class Solution:
    def minJumps(self, arr: List[int]) -> int:
        arr = [x for i, x in enumerate(arr) if i == 0 or i == len(arr) - 1 or x != arr[i - 1] or x != arr[i + 1]]

        d = {}
        for i, x in enumerate(arr):
            d.setdefault(x, set()).add(i)
        adj = {}
        for i, x in enumerate(arr):
            adj[i] = set()
            if i != 0:
                adj[i].add(i - 1)
            if i != len(arr) - 1:
                adj[i].add(i + 1)
            adj[i] |= d[arr[i]]
            adj[i].remove(i)

        q = collections.deque()
        distance = [len(arr) - 1] * len(arr)
        q.append(0)
        count = 0
        while q:
            nxt_q = collections.deque()
            while q:
                nxt = q.popleft()
                if distance[nxt] <= count:
                    continue
                distance[nxt] = count
                for x in adj[nxt]:
                    nxt_q.append(x)
            q = nxt_q
            count += 1
        return distance[-1]
