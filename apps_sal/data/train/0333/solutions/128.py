class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        idxs = defaultdict(list)
        for i, v in enumerate(arr):
            if (0 < i < n - 1 and arr[i - 1] == v == arr[i + 1]):
                continue
            idxs[v].append(i)

        q = deque([(0, 0)])
        visited = set()
        while q:
            i, cnt = q.popleft()
            visited.add(i)

            if i == len(arr) - 1:
                return cnt

            for j in [i - 1, i + 1]:
                if 0 <= j < n and j not in visited:
                    q.append((j, cnt + 1))

            for j in idxs[arr[i]]:
                if j != i and j not in visited:
                    q.append((j, cnt + 1))

        return -1
