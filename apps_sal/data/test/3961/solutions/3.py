n = int(input())
q, p = 1000000007, [0] + list(map(int, input().split()))
s, d = 0, [0] * (n + 1)
for i in range(1, n + 1):
    d[i] = (sum(d[p[i]: i]) + 2) % q
    s += d[i]
print(s % q)
