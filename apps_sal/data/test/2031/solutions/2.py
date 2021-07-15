n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    d = dict()
    k, pos = map(int, input().split())
    b = a + []
    for i in range(k):
        d[b.index(max(b))] = max(b)
        b[b.index(max(b))] = 0
    print(d[sorted(d.keys())[pos - 1]])
