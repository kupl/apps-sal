import sys
input = sys.stdin.readline


n, T = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))


for i in range(n):
    t[i] -= T

lower = []
upper = []
max_lower = 0
max_upper = 0
ans = 0
for i in range(n):
    if t[i] == 0:
        ans += a[i]
    elif t[i] < 0:
        lower.append((-t[i], a[i]))
        max_lower += abs(a[i] * t[i])
    else:
        upper.append((t[i], a[i]))
        max_upper += abs(a[i] * t[i])

max_heat = min(max_upper, max_lower)
lower.sort()
upper.sort()

tmp = 0
for ti, ai in lower:
    if tmp + ti * ai < max_heat:
        ans += ai
        tmp += ti * ai
    else:
        ans += (max_heat - tmp) / ti
        tmp = max_heat
tmp = 0
for ti, ai in upper:
    if tmp + ti * ai < max_heat:
        ans += ai
        tmp += ti * ai
    else:
        ans += (max_heat - tmp) / ti
        tmp = max_heat
print(ans)
