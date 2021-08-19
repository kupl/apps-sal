from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
dAl = defaultdict(int)
dAr = defaultdict(int)
for i in range(N):
    L = i + 1 + A[i]
    R = i + 1 - A[i]
    dAl[L] += 1
    dAr[R] += 1
ans = 0
for (k, v) in dAl.items():
    ans += v * dAr[k]
print(ans)
