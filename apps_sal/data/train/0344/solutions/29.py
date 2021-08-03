class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        l, m = len(A), len(A[0])
        f = [i for i in range(m)]
        f[0] = 0
        for i in range(1, m):
            for j in range(0, i):
                flag = True
                for k in range(l):
                    if A[k][j] > A[k][i]:
                        flag = False
                        break
                if flag:
                    f[i] = min(f[i], f[j] + i - j - 1)

        # print(f)
        # g = [f[i]+m-1-i for i in range(m)]
        # print(g)
        # return min(g)
        return min([f[i] + m - 1 - i for i in range(m)])
