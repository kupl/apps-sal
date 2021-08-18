import sys


def __starting_point():
    n = int(input())
    a = {}
    a_s = input().split()
    for i in range(n):
        x = n - int(a_s[i])
        a[x] = a.get(x, 0) + 1
        a_s[i] = x
    for i in a:
        if (i < 1) or (i > n):
            print("Impossible")
            return
        if a[i] % i != 0:
            print("Impossible")
            return
    print("Possible")
    used = 0
    col = {}
    num = {}
    b = []
    for x in a_s:
        if x not in col or num[x] == x:
            used += 1
            col[x] = used
            num[x] = 1
            b.append(used)
        else:
            num[x] += 1
            b.append(col[x])
    print(" ".join(map(str, b)))


__starting_point()
