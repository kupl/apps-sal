serch_table = []

for i in range(100):
    for j in range(1, 1000):
        x = str(j) + '9' * i
        x = int(x)
        serch_table.append(x)

L = []
for i in serch_table:
    l = [x for x in str(i)]
    x = sum(map(int, l))
    l = [i / x, i]
    L.append(l)
L = sorted(L)
M = []
tmp = -1
for i in L:
    if tmp < i[1]:
        M.append(i[1])
        tmp = i[1]
N = int(input())
for i in range(N):
    print((M[i]))
