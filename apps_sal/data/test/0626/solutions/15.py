n = int(input())
a = list(map(int, input().split()))
used = [False for i in range(n)]
k = 0

for i in range(n):
    flag = False
    for j in range(n):
        if a[j] <= k and used[j] == False:
            used[j] = True
            k += 1
    for j in range(n):
        if used[j] == False:
            flag = True
    if flag == False:
        print(2 * i)
        break
    for j in range(n - 1, -1, -1):
        if a[j] <= k and used[j] == False:
            used[j] = True
            k += 1
    flag = False
    for j in range(n):
        if used[j] == False:
            flag = True
    if flag == False:
        print(2 * i + 1)
        break
