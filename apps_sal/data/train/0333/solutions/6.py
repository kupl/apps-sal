class Solution:
    def minJumps(self, arr: List[int]) -> int:
        v2n = collections.defaultdict(set)
        for i, v in enumerate(arr):
            if 0 < i < len(arr) - 1 and arr[i - 1] == v and arr[i + 1] == v:
                continue
            v2n[v].add(i)
        visited, seen, q, step = set([0]), set(), collections.deque([0]), 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == len(arr) - 1:
                    return step
                neighbors = set([cur + 1, cur - 1] + [x for x in v2n[arr[cur]]])
                for nb in neighbors:
                    if nb >= 0 and nb < len(arr) and nb != cur and nb not in visited:
                        visited.add(cur)
                        q.append(nb)
                # seen.add(cur)
            step += 1
        return -1
