import bisect
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = 10000000000
    for i in range(n - k):
        if ans > a[i + k] - a[i]:
            ansindex = i
            ans = a[i + k] - a[i]
    print(a[ansindex] + ans // 2)
