import math


def test():
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = math.inf
    for i in range(len(a)):
        se = set()
        if i + d <= len(a):
            for j in range(i, i + d):
                se.add(a[j])
            ans = min(ans, len(se))
    print(ans)


def print2d(a):
    for i in a:
        print(' '.join(list(map(str, i))))


t = int(input())

for i in range(t):
    test()
