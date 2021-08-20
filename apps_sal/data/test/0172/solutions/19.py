n = int(input())
A = list(map(int, input().split()))
a = [0] * 6
B = list(map(int, input().split()))
b = [0] * 6
for i in A:
    if i == 1:
        a[1] += 1
    if i == 2:
        a[2] += 1
    if i == 3:
        a[3] += 1
    if i == 4:
        a[4] += 1
    if i == 5:
        a[5] += 1
for i in B:
    if i == 1:
        b[1] += 1
    if i == 2:
        b[2] += 1
    if i == 3:
        b[3] += 1
    if i == 4:
        b[4] += 1
    if i == 5:
        b[5] += 1
ans = 0
f = True
for i in range(1, 6):
    if (a[i] + b[i]) % 2 == 1:
        f = False
if f:
    for i in range(1, 6):
        ans += abs(a[i] - (a[i] + b[i]) // 2)
if f:
    print(ans // 2)
else:
    print(-1)
