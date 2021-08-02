from math import *
n, a, b = map(int, input().split())
x = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    ans[i] = x[i] - ceil(int(x[i] * a / b) * b / a)
print(*ans)
