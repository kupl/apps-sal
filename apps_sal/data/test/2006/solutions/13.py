ds = set()
n, m = map(int, input().split())
for i in range(n):
    r = input()
    d = r.index('S') - r.index('G')
    if d < 0:
        print(-1)
        return
    ds.add(d)
print(len(ds))
