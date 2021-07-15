n, k = map(int, input().split())
p = [0] * (n + 1)
for i in range(k):
    a, b, d = map(int, input().split())
    p[a] += d
    p[b] -= d
print(sum(map(abs, p)) // 2)
