import sys
input = sys.stdin.readline


def rInt():
    return int(input())


def mInt():
    return list(map(int, input().split()))


def rLis():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    (n, k) = mInt()
    a = rLis()
    b = rLis()
    a.sort()
    b.sort(reverse=True)
    for i in range(k):
        if a[i] < b[i]:
            a[i] = b[i]
    print(sum(a))
