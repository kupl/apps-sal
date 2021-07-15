##   int(input())
n, m= map(int,input().split())
a = list(map(int,input().split()))
tot = 0
rs = []
for i in range(m):
    t = list(map(int,input().split()))
    if t[0] == 1:
        v = t[1]
        x = t[2]
        a[v - 1] = x - tot
    if t[0] == 2:
        y = t[1]
        tot += y
    if t[0] == 3:
        q = t[1]
        rs.append(str(a[q - 1] + tot))
print('\n'.join(rs))
