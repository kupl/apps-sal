class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = collections.defaultdict(list)
        for i, num in enumerate(arr):
            g[num].append(i)
        visited = set()
        q = deque([(0, 0)])  # idx,step

        while q:
            idx, step = q.popleft()
            if idx == len(arr) - 1:
                return step
            visited.add(idx)
            for n_idx in [idx - 1, idx + 1] + g[arr[idx]]:
                if n_idx not in visited and 0 <= n_idx < len(arr):
                    q.append((n_idx, step + 1))
            del g[arr[idx]]
