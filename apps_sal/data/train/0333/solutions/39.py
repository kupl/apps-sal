class Solution:

    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        indices = collections.defaultdict(set)
        for (i, a) in enumerate(arr):
            indices[a].add(i)
        queue = collections.deque([(0, 0)])
        seen = {0}
        value_seen = set()
        while queue:
            (i, move) = queue.popleft()
            if i == N - 1:
                return move
            if arr[i] not in value_seen:
                value_seen.add(arr[i])
                for j in indices[arr[i]]:
                    if j != i and j not in seen:
                        seen.add(j)
                        queue.append((j, move + 1))
            if i - 1 >= 0 and i - 1 not in seen:
                seen.add(i - 1)
                queue.append((i - 1, move + 1))
            if i + 1 < N and i + 1 not in seen:
                seen.add(i + 1)
                queue.append((i + 1, move + 1))
