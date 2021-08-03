# ABC160
K, N = map(int, input().split())
A = list(map(int, input().split()))
a = [K - (A[N - 1] - A[0])]
for i in range(1, N):
    a.append(abs(A[i] - A[i - 1]))
print(K - max(a))
