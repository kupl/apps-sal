n, m = map(int, input().split())
L = []
for i in range(m):
    li = list(map(int, input().split()))
    L.append(li)

li = []
for i, j in enumerate(L):
    li.append(j + [i])
li.sort(key=lambda x: (x[0], x[1]))

li.append([0, 0, 0])

k, r = li[0][0], 1
for i in range(m):
    if li[i][0] == k:
        if li[i + 1][1] == li[i][1]:
            li[i][1] = r
            li[i + 1][1] = r
        else:
            li[i][1] = r
            r += 1
    else:
        k = li[i][0]
        r = 1
        li[i][1] = r
        r += 1

li.pop()

li.sort(key=lambda x: x[2])

for i in range(m):
    print("{:06d}".format(li[i][0]) + "{:06d}".format(li[i][1]))
