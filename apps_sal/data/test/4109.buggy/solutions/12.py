(N, M, X) = map(int, input().split())


def num2bi(num):
    l = [0] * N
    for i in range(N):
        if num >= 2 ** (N - 1 - i):
            num -= 2 ** (N - 1 - i)
            l[i] = 1
    return l


SUM = [0] * M
A = [[0] * M for _ in range(N)]
C = []
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        SUM[j] += a[j + 1]
        A[i][j] = a[j + 1]
    C.append(a[0])
ans = sum(C)
if min(SUM) < X:
    ans = -1
else:
    for num in range(2 ** N):
        SUM = [0] * M
        tmp = 0
        for i in range(N):
            if num2bi(num)[i] == 1:
                for j in range(M):
                    SUM[j] += A[i][j]
                tmp += C[i]
        if min(SUM) >= X:
            ans = min(ans, tmp)
print(ans)
