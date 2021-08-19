import sys
import math
input = sys.stdin.readline


def inp():
    return int(input())


def inara():
    return list(map(int, input().split()))


def insr():
    s = input()
    return list(s[:len(s) - 1])


def invr():
    return list(map(int, input().split()))


(n, k, p) = invr()
a = inara()
b = inara()
a.sort()
b.sort()
ans = int(1e+18)
for i in range(k - n + 1):
    curr = -1
    for j in range(n):
        if p <= b[i + j] and b[i + j] <= a[j]:
            curr = max(curr, a[j] - p)
        elif a[j] <= b[i + j] and b[i + j] <= p:
            curr = max(curr, p - a[j])
        else:
            curr = max(curr, abs(a[j] - b[i + j]) + abs(p - b[i + j]))
    ans = min(ans, curr)
print(ans)
