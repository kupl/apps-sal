class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        F = [0] * n
        d = collections.defaultdict(int)

        def find(x):
            if F[x] < 0:
                return x
            else:
                F[x] = find(F[x])
                return F[x]

        t = [0] * n
        ans = -1

        for i in range(n):
            ind = arr[i] - 1
            d[1] += 1
            t[ind] = 1
            F[ind] = -1
            if ind > 0 and t[ind - 1] == 1:
                new = find(ind - 1)
                d[-F[ind]] -= 1
                d[-F[new]] -= 1
                d[-F[ind] - F[new]] += 1
                F[ind] += F[new]
                F[new] = ind
            if ind < n - 1 and t[ind + 1] == 1:
                new = find(ind + 1)
                d[-F[ind]] -= 1
                d[-F[new]] -= 1
                d[-F[ind] - F[new]] += 1
                F[ind] += F[new]
                F[new] = ind
            if d[m] > 0:
                ans = i + 1
        return ans
