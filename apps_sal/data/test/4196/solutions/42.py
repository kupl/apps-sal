from math import gcd
N = int(input())
A = list(map(int, input().split()))
left = [0]
right = [0]
for i in range(1, N + 1):
    l = gcd(left[-1], A[i - 1])
    left.append(l)
    r = gcd(right[-1], A[N - i])
    right.append(r)
res = 0
for i in range(N):
    res = max(res, gcd(left[i], right[N - i - 1]))
print(res)
