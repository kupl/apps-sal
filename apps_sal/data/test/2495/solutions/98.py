n = int(input())
a = list(map(int, input().split()))
if a[0] == 0:
    ans1 = 1
    tmp = 1
else:
    ans1 = 0
    tmp = a[0]
is_plus = tmp > 0
for i in range(1, n):
    tmp += a[i]
    if is_plus == (tmp > 0):
        ans1 += abs(tmp) + 1
        if is_plus:
            tmp = -1
        else:
            tmp = 1
        is_plus = tmp > 0
    else:
        is_plus = tmp > 0
ans2 = abs(a[0]) + 1
if a[0] == 0:
    ans2 = 1
    tmp = -1
else:
    ans2 = abs(a[0]) + 1
    tmp = -a[0] // abs(a[0])
is_plus = tmp > 0
for i in range(1, n):
    tmp += a[i]
    if is_plus == (tmp > 0):
        ans2 += abs(tmp) + 1
        if is_plus:
            tmp = -1
        else:
            tmp = 1
        is_plus = tmp > 0
    else:
        is_plus = tmp > 0
print(min(ans1, ans2))
