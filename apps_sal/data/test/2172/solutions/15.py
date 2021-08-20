(n, m) = map(int, input().split())
d = {}
for i in range(m):
    (a, b) = input().split()
    d[a] = b
for s in input().split():
    if len(s) > len(d[s]):
        print(d[s], end=' ')
    else:
        print(s, end=' ')
