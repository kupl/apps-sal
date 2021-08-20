class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        counts = defaultdict(int)
        root = [i for i in range(len(arr))]
        size = [0 for i in range(len(arr))]
        rank = [1 for i in range(len(arr))]

        def find(i):
            if root[i - 1] != i - 1:
                root[i - 1] = find(root[i - 1] + 1)
            return root[i - 1]

        def union(i, j):
            pi = find(i)
            pj = find(j)
            length = size[pi] + size[pj]
            if pi != pj:
                if rank[pi] <= rank[pj]:
                    root[pi] = pj
                    if rank[pi] == rank[pj]:
                        rank[pj] += 1
                else:
                    root[pj] = pi
                size[root[pi]] = length
        step = -1
        for i in range(len(arr)):
            size[arr[i] - 1] += 1
            if arr[i] - 1 != 0 and size[find(arr[i] - 1)] != 0:
                counts[size[find(arr[i] - 1)]] -= 1
                union(arr[i] - 1, arr[i])
            if arr[i] + 1 != len(arr) + 1 and size[find(arr[i] + 1)] != 0:
                counts[size[find(arr[i] + 1)]] -= 1
                union(arr[i] + 1, arr[i])
            counts[size[find(arr[i])]] += 1
            if counts[m] != 0:
                step = i + 1
        return step
    '\n    [5,3,4,7,8,14,11,9,2,12,1,13,10,6]\n6\n    '
