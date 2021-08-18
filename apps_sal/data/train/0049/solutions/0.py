
import sys
input = sys.stdin.readline


classy = set()

for i in range(19):
    for j in range(i):
        for k in range(j):
            for a in range(10):
                for b in range(10):
                    for c in range(10):
                        what = a * 10**i + b * 10**j + c * 10**k
                        classy.add(what)

li = sorted(classy)


def counting(i):
    lo = 0
    hi = len(li) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if li[mid] <= i:
            lo = mid
        else:
            hi = mid - 1
    return lo


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(counting(b) - counting(a - 1))
