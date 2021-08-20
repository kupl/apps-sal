class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 1:
            return 0
        mat = [[0 for i in range(l)] for i in range(l)]
        for i in range(l - 1):
            mat[i][i + 1] = arr[i] ^ arr[i + 1]
            for j in range(i + 2, l):
                mat[i][j] = mat[i][j - 1] ^ arr[j]
        count = 0
        for i in range(l):
            for j in range(i + 1, l):
                curr = mat[i][j - 1]
                if i + 1 == j:
                    curr = arr[i]
                for k in range(j, l):
                    pres = mat[j][k]
                    if j == k:
                        pres = arr[j]
                    if curr == pres:
                        count += 1
        return count
