# 36 C - Skip
import bisect
import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
x = sorted(x, reverse=False)

bisect.insort_left(x, X)
# 間隔の最小の素数
d_lis = []
for i in range(len(x) - 1):
    d = x[i + 1] - x[i]
    d_lis.append(d)
d_lis = sorted(d_lis, reverse=False)

ans = d_lis[0]
for j in range(1, len(d_lis)):
    ans = math.gcd(ans, d_lis[j])
print(ans)
