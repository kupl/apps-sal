def count(n, c, a):
    vis = [0] * (n + 1)
    z = []
    p = []
    for i in range(1, n + 1):
        x = i
        while vis[x] == 0:
            vis[x] = i
            x = a[x - 1]
        if vis[x] == i:
            p.append(x)
    return p


def opium(n, c, a):
    sum = 0
    p = list(set(count(n, c, a)))
    for x in p:
        v = x
        cd = c[x - 1]
        while v != a[x - 1]:
            x = a[x - 1]
            cd = min(cd, c[x - 1])
        sum = sum + cd
    return sum


def main():
    n = int(input())
    c = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    return opium(n, c, a)


print(main())
