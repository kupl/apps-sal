n, m, k = map(int, input().split())
s, c = 0, 0
R = [list(map(int, input().split())) for i in range(n)]
for i in zip(*R):
    a, b = 0, 0
    for j in range(n - k + 1):
        f, h = sum(i[j:j + k]), sum(i[:j])
        if f > a:
            a, b = f, h
    s += a
    c += b
print(s, c, end=' ')
