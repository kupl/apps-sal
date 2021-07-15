n, m = list(map(int, input().split()))
c = [list(input()) for _ in range(n)]

ans = "NO"
if n % 3 == 0:
    l = []
    for i in range(3):
        s = set([])
        for j in range(i * n // 3, (i + 1) * n // 3):
            for k in range(m):
                s.add(c[j][k])
        if len(s) == 1:
            l.append(s.pop())
    if sorted(l) == ['B', 'G', 'R']:
        ans = "YES"
if m % 3 == 0:
    l = []
    for i in range(3):
        s = set([])
        for j in range(i * m // 3, (i + 1) * m // 3):
            for k in range(n):
                s.add(c[k][j])
        if len(s) == 1:
            l.append(s.pop())
    if sorted(l) == ['B', 'G', 'R']:
        ans = "YES"

print(ans)

