n, m = map(int, input().split())
x = [0] * n
y = [0] * n
z = [0] * n
for i in range(n):
    x[i], y[i], z[i] = map(int, input().split())

sign = [0] * 3
ans = 0
for i in range(8):
    for j in range(3):
        if ((i >> j) & 1):
            sign[j] = 1
        else:
            sign[j] = -1
    tot = 0
    arr = [0] * n
    for k in range(n):
        arr[k] = x[k] * sign[0] + y[k] * sign[1] + z[k] * sign[2]
    arr = sorted(arr, reverse=True)
    tot = sum(arr[:m])
    if tot > ans:
        ans = tot
print(ans)
