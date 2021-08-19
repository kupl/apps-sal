N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])

ans = -1
for i in range(1 << N):  # range(0,2^N)　左ビットシフト
    A_sum = [0] * M  # t=[0 0 0]など len(t)=M
    C_sum = 0
    for j in range(N):
        if (i >> j) & 1 == 0:  # jのフラグがないとき
            continue
        C_sum += C[j]  # 合計の値段
        for k in range(M):
            A_sum[k] += A[j][k]  # 合計の理解度
    if all(x >= X for x in A_sum):  # tのすべての要素がXより大きいとき
        if ans == -1:
            ans = C_sum
        else:
            ans = min(ans, C_sum)
print(ans)
