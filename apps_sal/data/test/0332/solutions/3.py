def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n, m = mi()
a = [li() for i in range(n)]
b = [li() for i in range(n)]
p = [[] for i in range(n + m)]
q = [[] for i in range(n + m)]
for i in range(n):
    for j in range(m):
        p[i + j].append(a[i][j])
        q[i + j].append(b[i][j])
print('YES' if all(sorted(x) == sorted(y) for x, y in zip(p, q)) else 'NO')
