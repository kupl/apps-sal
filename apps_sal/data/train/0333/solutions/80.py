class Solution:

    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        last_idx = N - 1
        indices = collections.defaultdict(set)
        for (i, a) in enumerate(arr):
            indices[a].add(i)
        moves = [None] * N
        moves[0] = 0
        edges = []
        idx = 0
        seen_values = set()

        def reachables(i):
            idx_set = set()
            if arr[i] not in seen_values:
                seen_values.add(arr[i])
                idx_set |= indices[arr[i]]
            if i - 1 >= 0:
                idx_set.add(i - 1)
            if i + 1 < N:
                idx_set.add(i + 1)
            if i in idx_set:
                idx_set.remove(i)
            return idx_set
        while idx != last_idx:
            for j in reachables(idx):
                if moves[j] is None:
                    heapq.heappush(edges, (moves[idx] + 1, j))
            (move, idx) = heapq.heappop(edges)
            moves[idx] = move
        return moves[idx]
