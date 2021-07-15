n = int(input())
a = [int(x) for x in input().split()]
k = 0
pov = 0
used = [False] * n
for i in range(n):
    for j in range(n):
        if used[j] == False and a[j] <= k:
            used[j] = True
            k += 1
    r = 0
    for j in range(n):
        if used[j] == False:
            r = 1
    if r == 0:
        print(pov)
        break
    else:
        pov += 1
    for j in range(n - 1, -1, -1):
        if used[j] == False and a[j] <= k:
            used[j] = True
            k += 1
    r = 0
    for j in range(n):
        if used[j] == False:
            r = 1
    if r == 0:
        print(pov)
        break
    else:
        pov += 1
