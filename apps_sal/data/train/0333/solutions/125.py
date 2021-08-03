class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = {0}
        lookup = defaultdict(list)
        for i, val in enumerate(arr):
            lookup[val].append(i)

        deq = deque([(0, 0)])

        while deq:
            i, step = deq.popleft()
            if i == len(arr) - 1:
                return step
            nxt_idx = [i - 1, i + 1]
            nxt_idx.extend(lookup[arr[i]])
            lookup[arr[i]] = []
            for nxt in nxt_idx:
                if 0 <= nxt < len(arr) and nxt not in visited:
                    deq.append((nxt, step + 1))
                    visited.add(nxt)
        return 0
