from sys import stdin


def iinput():
    return int(stdin.readline())


def minput():
    return list(map(int, stdin.readline().split()))


def linput():
    return list(map(int, stdin.readline().split()))


t = iinput()
while t:
    t -= 1
    (n, k) = minput()
    a = linput()
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += max(0, k - a[i]) // a[0]
    print(ans)
