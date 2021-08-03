class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        #0 <= i < j < k <= n
        #xor(arr[i:j]) == xor[j:k]
        d = {}
        xormat = [[0] * (n + 1) for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                xormat[i][j] = v = xormat[i][j - 1] ^ arr[j - 1]
                if v in d:
                    d[v].append((i, j))
                else:
                    d[v] = [(i, j)]
        count = 0
        # print(d)
        from collections import defaultdict
        for values in list(d.values()):
            counts = defaultdict(list)
            for i, j in values:
                counts[i].append(j)
            for v in values:
                count += len(counts[v[1]])
        return count
