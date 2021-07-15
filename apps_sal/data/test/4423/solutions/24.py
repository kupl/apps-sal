n = int(input())
tbl = []

for i in range(n):
    l = list(map(str,input().split()))
    l[1] = int(l[1])
    l2 = [l[1], l[0], i + 1]
    tbl.append(l2)

tbl.sort(key = lambda x:(x[1], -x[0]))
for i in range(n):
    print((tbl[i][2]))

