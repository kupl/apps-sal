n, m = list(map(int, input().split()))
row = set()
col = set()
s = ""
for i in range(m):
    r, c = list(map(int, input().split()))
    row.add(r)
    col.add(c)
    dead = len(row)*n+len(col)*(n-len(row))
    s += str(n*n - dead) + " "
print(s)

