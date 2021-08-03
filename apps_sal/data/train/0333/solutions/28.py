class Solution:
    def minJumps(self, arr: List[int]) -> int:

        to_index = {}
        for i in range(len(arr)):
            if arr[i] not in to_index:
                to_index[arr[i]] = []
            to_index[arr[i]].append(i)

        n = len(arr)
        q = [(0, 0)]
        vis = set([0])

        for i, jumps in q:
            if i == n - 1:
                return jumps
            if i + 1 < n and i + 1 not in vis:
                vis.add(i + 1)
                q.append((i + 1, jumps + 1))
            if i - 1 >= 0 and i - 1 not in vis:
                vis.add(i - 1)
                q.append((i - 1, jumps + 1))
            for j in to_index[arr[i]]:
                if j not in vis:
                    q.append((j, jumps + 1))
                    vis.add(j)
            to_index[arr[i]] = []
        return -1
