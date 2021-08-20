(n, q) = map(int, input().split())
arr = []
ff = [0] * 5005
for i in range(q):
    (x, y) = map(int, input().split())
    for j in range(x, y + 1):
        ff[j] += 1
    arr.append([x, y])
ans = 0
for i in range(q):
    tt = 0
    for j in range(arr[i][0], arr[i][1] + 1):
        ff[j] -= 1
    for j in range(5005):
        if ff[j] > 0:
            tt += 1
    c = [0] * (n + 1)
    for j in range(1, n + 1):
        c[j] = c[j - 1]
        if ff[j] == 1:
            c[j] += 1
    for j in range(i + 1, q):
        ans = max(ans, tt - c[arr[j][1]] + c[arr[j][0] - 1])
    for j in range(arr[i][0], arr[i][1] + 1):
        ff[j] += 1
print(ans)
