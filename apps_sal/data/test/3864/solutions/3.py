Q = 998244353
N = int(input())
a = range(N)
C = (Q + 1) // 2
p = [N * C] * N * 3
q = [1] * N * 2
for i in a:
    q[i + 1] = (q[i] * C) % Q
for i in a:
    p[i + 2] = p[i + 1] + q[N - 2 * i - 1] * (2 * i + 3)
    print(p[min(i, N - 1 - i)] % Q)
