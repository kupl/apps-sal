N = int(input())
A = list(map(int, input().split()))
to = [0] * N
for i in range(N - 1):
    if i == 0:
        SUM = A[i]
    else:
        SUM -= A[i - 1]
    for j in range(min(to[i - 1] + 1, N - 1), N):
        if SUM + A[j] != SUM ^ A[j]:
            to[i] = j - 1
            break
        if j == N - 1:
            to[i] = j
            break
        SUM += A[j]
print(sum([max(0, to[i] - i) for i in range(N)]) + N)
