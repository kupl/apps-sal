N, K, M = map(int, input().split())
A = list(map(int, input().split()))

SUM = 0
AVG = 0
A_N = 0

while AVG <= M:
    for i in range(0, N - 1):
        SUM += A[i]

    SUM += A_N
    AVG = int(SUM / N)
    if AVG >= M:
        break
    SUM = 0
    A_N += 1

if A_N > K:
    print('-1')
else:
    print(A_N)
