(N, K) = list(map(int, input().split()))
A = [int(a) for a in input().split()]
B = [0] * N
B[N - 1] = A[N - 1]
for i in range(N - 1)[::-1]:
    B[i] = B[i + 1] + A[i]
print(sum(sorted(B[1:])[::-1][:K - 1]) + B[0])
