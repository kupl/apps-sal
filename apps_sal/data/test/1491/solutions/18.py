import math
n = int(input())
arr = list(map(int, input().split()))
checks = []
zc = 0
for i in arr:
    x = i ** 0.5
    if int(x) * int(x) == i:
        checks.append(0)
        if not i:
            zc += 1
    else:
        l = math.ceil(x)
        m = math.floor(x)
        checks.append(min(abs(l * l - i), abs(i - m * m)))
checks.sort()
marks = n // 2
if checks.count(0) == marks:
    print(0)
elif checks.count(0) < marks:
    l = checks.count(0)
    s = 0
    while l < marks:
        s += checks[l]
        l += 1
    print(s)
else:
    l = checks.count(0)
    non_zero_sq = l - zc
    non_sq = n - l
    ans = 0
    marks -= non_sq
    while non_zero_sq > 0 and marks > 0:
        marks -= 1
        non_zero_sq -= 1
        ans += 1
    while marks > 0 and zc > 0:
        zc -= 1
        marks -= 1
        ans += 2
    print(ans)
