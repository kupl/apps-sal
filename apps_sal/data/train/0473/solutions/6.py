class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        pool = dict()
        pool[(0, 0)] = 0
        pool[(1, 1)] = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (i, j) not in pool:
                    a = pool[(i, j - 1)] ^ arr[j - 1]
                    pool[(i, j)] = a
                else:
                    a = pool[(i, j)]
                for k in range(j, len(arr)):
                    if (j, k + 1) not in pool:
                        if j == k:
                            b = arr[k]
                        else:
                            b = pool[(j, k)] ^ arr[k]
                        pool[(j, k + 1)] = b
                    else:
                        b = pool[(j, k + 1)]
                    if a == b:
                        ans += 1
        return ans
