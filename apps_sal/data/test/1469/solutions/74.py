l = int(input())
n = l.bit_length()
edge = list()
for i in range(1, n):
    edge.append((i, i + 1, 0))
    edge.append((i, i + 1, 1 << (i - 1)))
t = l - (1 << (n - 1))
cnt = (n - 1) * 2
while t:
    m = t.bit_length()
    edge.append((m, n, l - t))
    t -= (1 << m - 1)
    cnt += 1
print(n, cnt)
for t in edge:
    print(*t)
