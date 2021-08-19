import sys
input = sys.stdin.readline


def I():
    return list(map(int, input().split()))


(t,) = I()
for i in range(t):
    (n,) = I()
    a = I()
    l = I()
    ar = [a[i] for i in range(n) if l[i] == 0]
    ar.sort(reverse=True)
    x = 0
    for i in range(n):
        if l[i] == 0:
            a[i] = ar[x]
            x += 1
    print(*a)
