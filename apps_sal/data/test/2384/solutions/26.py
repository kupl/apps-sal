n = int(input())
arr = list(map(int, input().split()))
acum1 = [0]
acum2 = [0]
for i in range(n):
    if i % 2 == 0:
        acum1.append(acum1[-1] + arr[i])
        acum2.append(acum2[-1] + 0)
    else:
        acum1.append(acum1[-1] + 0)
        acum2.append(acum2[-1] + arr[i])
if n % 2 == 0:
    ans = max(acum1[n - 1] - acum1[0], acum2[n] - acum2[1])
    for i in range(1, n + 1, 2):
        if i + 3 > n:
            continue
        tmp = acum1[i] - acum1[0] + (acum2[n] - acum2[i + 2])
        ans = max(ans, tmp)
else:
    ans = max(acum1[n - 2] - acum1[0], acum2[n - 1] - acum2[1], acum1[n] - acum1[2])
    for i in range(1, n + 1, 2):
        if i + 3 > n - 1:
            continue
        tmp = acum1[i] - acum1[0] + (acum2[n - 1] - acum2[i + 2])
        ans = max(ans, tmp)
    for i in range(2, n + 1, 2):
        if i + 3 > n:
            continue
        tmp = acum2[i] - acum2[1] + (acum1[n] - acum1[i + 2])
        ans = max(ans, tmp)
    for i in range(1, n + 1, 2):
        if i + 4 > n:
            continue
        tmp = acum1[i] - acum1[0] + (acum1[n] - acum1[i + 3])
        ans = max(ans, tmp)
    acummax = [-10 ** 18]
    for i in range(1, n + 1):
        if i + 2 > n:
            acummax.append(-10 ** 18)
        elif i % 2 == 0:
            acummax.append(acum2[i] + acum1[n] - acum1[i + 2])
        else:
            acummax.append(-10 ** 18)
    for i in range(n - 1, -1, -1):
        acummax[i] = max(acummax[i], acummax[i + 1])
    for i in range(1, n + 1, 2):
        if i + 6 > n:
            continue
        tmp = acum1[i] - acum1[0] - acum2[i + 2] + acummax[i + 3]
        ans = max(ans, tmp)
print(ans)
