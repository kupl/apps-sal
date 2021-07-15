from math import *

n, r = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = []

for i in range(n):
    yi = r
    for j in range(i):
        if abs(x[j] - x[i]) <= 2 * r:
            yi = max(yi, ans[j] + sqrt(4 * r**2 - (x[j] - x[i])**2))
    ans.append(yi)
print(' '.join(map(str, ans)))

