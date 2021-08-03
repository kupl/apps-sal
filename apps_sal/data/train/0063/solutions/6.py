import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    n = list(map(int, input().split()))
    w = list(map(int, input().split()))

    n.sort(reverse=True)
    w.sort()

    ans = 0
    for j in range(b):
        ans += n[j]
        if w[j] == 1:
            ans += n[j]

    ind = b - 1

    for j in range(b):
        if w[j] > 1:
            ind += w[j] - 1
            ans += n[ind]

    print(ans)
