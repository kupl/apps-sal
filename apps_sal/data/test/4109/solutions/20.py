(N, M, X) = list(map(int, input().split()))
B = [0] * N
for i in range(N):
    B[i] = list(map(int, input().strip().split()))
x = N * 10 ** 10
sum_ok = N * 10 ** 10
unst = [0] * M
flg = 0


def all0(v):
    return 0


for i in range(2 ** N):
    sum = 0
    unst = list(map(all0, unst))
    for j in range(N):
        if i >> j & 1:
            sum += B[j][0]
            for k in range(M):
                unst[k] += B[j][k + 1]
    if all((elem >= X for elem in unst)):
        sum_ok = sum
        flg = 1
    x = min(x, sum_ok)
if flg == 0:
    print(-1)
else:
    print(x)
