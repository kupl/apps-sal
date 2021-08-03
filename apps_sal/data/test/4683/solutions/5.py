N = int(input())
A = list(map(int, input().split()))
A2 = [A[0]]
mod = 10 ** 9 + 7
res = 0
for i in range(1, N):
    A2.append((A2[i - 1] + A[i]) % mod)
for i in range(N - 1):
    res = (res + A[i] * (A2[N - 1] - A2[i])) % mod
print(res)
