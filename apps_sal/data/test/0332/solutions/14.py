n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
aa = [[] for _ in range(n + m)]
bb = [[] for _ in range(n + m)]
for i in range(n):
    for k in range(m):
        aa[i + k].append(a[i][k])
        bb[i + k].append(b[i][k])
print("YES" if all(map(lambda x, y: sorted(x) == sorted(y), aa, bb)) else "NO")
