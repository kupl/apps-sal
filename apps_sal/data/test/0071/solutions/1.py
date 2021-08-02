n, m, k, x, y = map(int, input().split())

arr = [[0 for i in range(m)] for j in range(n)]

if(n == 1):
    loop = k // m
    for i in range(m):
        arr[0][i] += loop
    rest = k % m

    i = 0
    j = 0
    while(rest > 0):
        arr[i][j] += 1
        j += 1
        if(j == m):
            i += 1
            j = 0
        rest -= 1

    print(max(arr[0]), min(arr[0]), arr[x - 1][y - 1])
    return

loop = k // ((n * 2 - 2) * m)

for i in range(m):
    arr[0][i] += loop
    for j in range(1, n - 1):
        arr[j][i] += loop * 2
    arr[n - 1][i] += loop

rest = k % ((n * 2 - 2) * m)


i = 0
j = 0
while(rest > 0):
    arr[i][j] += 1
    rest -= 1
    j += 1
    if(j == m):
        j = 0
        i += 1
        if(i == n):
            break

i = n - 2
j = 0
while(rest > 0):
    arr[i][j] += 1
    rest -= 1
    j += 1
    if(j == m):
        j = 0
        i -= 1

mx = 0
mn = 100000000000000000000000
for i in range(n):
    mx = max(mx, max(arr[i]))
    mn = min(mn, min(arr[i]))


print(mx, mn, arr[x - 1][y - 1])
