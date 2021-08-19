N = 10 ** 5 + 1
(n, x) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [0] * N
for a in A:
    B[a] += 1
res = 0
for i in range(N):
    if i ^ x < N:
        res += B[i] * B[i ^ x]
print((res - n) // 2 if x == 0 else res // 2)
