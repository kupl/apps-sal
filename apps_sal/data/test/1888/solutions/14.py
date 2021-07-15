n, m = map(int, input().split())
p = [0] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    p[a], p[b] = p[a] - c, p[b] + c
print(sum(x for x in p if x > 0))
