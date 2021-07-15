import sys
import copy

N = int(input())
A = list(map(int, input().split()))
a = copy.deepcopy(A)
b = copy.deepcopy(A)

s = 0
cost_p = 0
cost_m = 0

for i in range(N):
    if i%2 == 0:
        new = max(abs(s) + 1, a[i])
        cost_p += new - a[i]
        a[i] = new
        s += a[i]
    else:
        new = min((-1)*abs(s) - 1, a[i])
        cost_p += abs(new - a[i])
        a[i] = new
        s += a[i]

s = 0

for i in range(N):
    if i%2 == 1:
        new = max(abs(s) + 1, b[i])
        cost_m += abs(new - b[i])
        b[i] = new
        s += b[i]
    else:
        new = min((-1)*abs(s) - 1, b[i])
        cost_m += abs(new - b[i])
        b[i] = new
        s += b[i]

print(min(cost_p, cost_m))
