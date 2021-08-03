class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if arr[-1] == arr[0]:
            return 1
        mapping = collections.defaultdict(list)
        for i, num in enumerate(arr):
            mapping[num].append(i)
        q = collections.deque([(0, 0)])
        visited = set([0])
        while q:
            cur_i, jumps = q.popleft()
            if cur_i == n - 1:
                return jumps
            curnum = arr[cur_i]
            for nei_i in mapping[curnum]:
                if nei_i != cur_i and nei_i not in visited:
                    visited.add(nei_i)
                    q.append((nei_i, jumps + 1))
            # clear the neighbors, since we have tried every
            # jumping ways in this mapping and we do not to
            # jump back
            mapping[curnum] = []
            if cur_i + 1 < n and cur_i + 1 not in visited:
                visited.add(cur_i + 1)
                q.append((cur_i + 1, jumps + 1))
            if cur_i - 1 >= 0 and cur_i - 1 not in visited:
                visited.add(cur_i - 1)
                q.append((cur_i - 1, jumps + 1))
        return -1
