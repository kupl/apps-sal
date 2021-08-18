import sys

n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
ub, lb = 0, 0
ans = 0

for x in a:
    if x == 0:
        if ub < 0:
            ub, lb = d, 0
            ans += 1
        lb = max(lb, 0)
    else:
        ub = min(d, ub + x)
        lb += x
        if lb > d:
            print(-1)
            return
print(ans)
