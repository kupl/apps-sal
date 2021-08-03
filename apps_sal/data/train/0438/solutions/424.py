class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        d = {}
        sizes = {}
        last_seen = -1

        def find(x):
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]
        for i in range(len(arr)):
            I = arr[i]
            d[I] = I
            size = 1
            if I - 1 in d:
                if sizes[find(I - 1)] == m:
                    last_seen = i
                d[find(I)] = I - 1
                sizes[find(I)] += size
                size = sizes[find(I)]
            if I + 1 in d:
                if sizes[find(I + 1)] == m:
                    last_seen = i
                d[find(I)] = I + 1
                sizes[find(I)] += size
                size = sizes[find(I)]
            sizes[find(I)] = size
            if size == m:
                last_seen = i + 1
        return last_seen
