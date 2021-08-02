x = int(input())
m = list(map(int, input().split()))
a = [[-1791791791] * 4 for i in range(x)]
a[0][0] = 0
if m[0] & 1:
    a[0][1] = 1
if m[0] & 2:
    a[0][2] = 1
for i in range(1, x):
    a[i][0] = max(a[i - 1])
    for j in range(1, 3):
        if m[i] & j:
            a[i][j] = max(a[i - 1][:j] + a[i - 1][j + 1:]) + 1
maxx = max(a[-1])
print(x - maxx)
