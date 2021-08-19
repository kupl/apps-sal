(n, m) = map(int, input().split())
p = [0] * (n + 1)
for i in range(m):
    (a, b, d) = map(int, input().split())
    p[a] += d
    p[b] -= d
print(sum((abs(i) for i in p)) // 2)
