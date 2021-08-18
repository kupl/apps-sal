n, m = map(int, input().split())
s_lis = []

for i in range(2 ** n):
    lis = []
    for j in range(len(bin(2 ** n)) - 3):
        if (i >> j) & 1:
            lis.append(1)
        else:
            lis.append(0)

    s_lis.append(lis)

b_lis = []
for k in range(m):
    b_lis.append(list(map(int, input().split())))

light = list(map(int, input().split()))

cnt = 0
for s in s_lis:
    c_lis = []
    for b in b_lis:
        c = 0
        for x in range(b[0]):
            c += s[b[x + 1] - 1]
        c_lis.append(c)

    c_lis = list(map(lambda y: y % 2, c_lis))
    if c_lis == light:
        cnt += 1

print(cnt)
