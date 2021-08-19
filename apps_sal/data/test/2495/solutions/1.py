n = int(input())
a = list(map(int, input().split()))
ans1 = 0
s = 0
for (i, v) in enumerate(a):
    if i % 2 and s + v >= 0:
        ans1 += abs(-1 - s - v)
        s = -1
    elif i % 2 == 0 and s + v <= 0:
        ans1 += abs(1 - s - v)
        s = 1
    else:
        s += v
s = 0
ans2 = 0
for (i, v) in enumerate(a):
    if i % 2 and s + v <= 0:
        ans2 += abs(1 - s - v)
        s = 1
    elif i % 2 == 0 and s + v >= 0:
        ans2 += abs(-1 - s - v)
        s = -1
    else:
        s += v
print(min(ans1, ans2))
