n, m = [int(x) for x in input().split()]
l = []

for i in range(n):
    row = [int(x) for x in input().split()]
    l.append( row )

found = False
for i in range(n):
    for j in range(m):
        if l[i][j]==1:
            if i==0 or i==n-1 or j==0 or j==m-1:
                found = True
                print("2")
                break
    if found:
        break

if not found:
    print("4")

