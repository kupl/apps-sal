class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        res = [[0]*(N+1) for _ in range(K)]
        # 初始化第一行
        for i in range(N+1):
            res[0][i] = i;
        # 从第二行开始
        if K == 1:
            return N
        for k in range(1,K):
            j = 1
            for i in range(1, N+1):
                while j < i+1 and res[k-1][j-1] < res[k][i-j]:
                    j += 1
                res[k][i] = 1 + res[k-1][j-1]
                # for j in range(1,i+1):
                #     if res[k-1][j-1] == res[k][i-j]:
                #         res[k][i] = 1 + res[k-1][j-1]
                #     else:
                #         continue
        # print(res) 
        return int(res[K-1][N])

