n, m, q = map(int, input().split(" "))
l = []


def maxx(l):
    cmax = 0
    count = 0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 1:
                count += 1
                if j == (len(l[i]) - 1) and count > cmax:
                    cmax = count
            else:
                if count > cmax:
                    cmax = count
                count = 0
        count = 0
    return cmax


def maxi(l):
    c = 0
    cmax = 0
    for i in range(len(l)):
        if l[i] == 1:
            c += 1
            if c > cmax:
                cmax = c
        else:
            c = 0
    return cmax


for i in range(n):
    li = list(map(int, input().split(" ")))
    l.append(li)

foo = []

for i in range(len(l)):
    foo.append(maxi(l[i]))

for i in range(q):
    i, j = map(int, input().split(" "))
    l[i - 1][j - 1] = 1 - l[i - 1][j - 1]
    foo[i - 1] = maxi(l[i - 1])

    print(max(foo))
