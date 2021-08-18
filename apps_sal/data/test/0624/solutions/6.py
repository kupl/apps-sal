N, K, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A = sorted(A)
maxavg = sum(A) / len(A)


ss = sum(A)


for i in range(min(N, M + 1)):
    if i > 0:
        ss = ss - A[i - 1]

    maxadvg = min(K * (N - i), M - i)

    maxavg = max(maxavg, (ss + maxadvg) / (N - i))

print(maxavg)
