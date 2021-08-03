n = int(input())
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
    c[i].append(i + 1)

r = int(input())
k = list(map(int, input().split()))


def sortfn(inp):
    return inp[1]


c.sort(key=sortfn, reverse=True)
for i in range(len(k)):
    val = k[i]
    k[i] = [i + 1, val]
k.sort(key=sortfn)


def gettable(size):
    for i in range(len(k)):
        if k[i][1] >= size:
            k[i][1] = -1
            table = k[i][0]
            return table
    return -1


groups = []
val = 0
for group in c:
    table = gettable(group[0])
    if table > 0:
        groups.append([str(group[2]), str(table)])
        val += group[1]

print(str(len(groups)) + " " + str(val))
for g in groups:
    print(" ".join(g))
