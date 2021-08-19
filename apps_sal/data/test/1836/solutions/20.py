n, m = list(map(int, input().split()))
gro = [[] * n for i in range(n)]
grno = [[] * n for i in range(n)]
ln = [1] * n
for i in range(m):
    x, y = list(map(int, input().split()))
    if x < y:
        gro[x - 1].append(y - 1)
    else:
        gro[y - 1].append(x - 1)
    grno[x - 1].append(y - 1)
    grno[y - 1].append(x - 1)
for i in range(n):
    for j in gro[i]:
        if ln[j] <= ln[i] + 1:
            ln[j] = ln[i] + 1
# for i in range(n):
#    print(gro[i])
# print("+___+")
# for i in range(n):
#    print(grno[i])
# print("+___+")
# print(ln)
mx = 0
for i in range(n):
    if ln[i] * len(grno[i]) > mx:
        mx = ln[i] * len(grno[i])
print(mx)
