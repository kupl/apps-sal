
import math


def rints():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n, m = rints()
    a = rints()
    p = rints()

    for _ in range(100):
        for pi in p:
            if a[pi - 1] > a[pi]:
                a[pi], a[pi - 1] = a[pi - 1], a[pi]

    print("YES" if sorted(a[:]) == a else "NO")
