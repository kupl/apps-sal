n = int(input())


def inp(n):
    coor = [[int(i) for i in input().split()] for j in range(n)]
    return coor


coor = inp(n)


def newlist(a):
    d = {}
    s = len(a)
    for i in range(1, s):
        for j in range(i):
            if (a[i][0] + a[j][0], a[i][1] + a[j][1]) in d:
                d[a[i][0] + a[j][0], a[i][1] + a[j][1]] += 1
            else:
                d[a[i][0] + a[j][0], a[i][1] + a[j][1]] = 1
    return d


def newd(d):
    sum2 = 0
    for l in d:
        sum2 += d[l] * (d[l] - 1) / 2
    return int(sum2)


print(newd(newlist(coor)))
