import sys


def main():
    (n, s) = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    l = 0
    r = n
    bestk = 0
    bests = 0
    while l < r:
        mid = (l + r) // 2
        x = [a[i] + (i + 1) * mid for i in range(n)]
        x.sort()
        t = 0
        for i in range(mid):
            t += x[i]
        if t <= s:
            bests = t
            bestk = mid
            l = mid + 1
        else:
            r = mid - 1
    mid = l
    x = [a[i] + (i + 1) * mid for i in range(n)]
    x.sort()
    t = 0
    for i in range(mid):
        t += x[i]
    if t <= s:
        bestk = mid
        bests = t
    print(bestk, bests)


main()
