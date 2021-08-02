n = int(input())
t = list(map(int, input().split()))
tem = int(input())
t.sort()
rmax = 1
for cont in range(0, n - 1):
    r = 1
    for cont2 in range(cont + 1, n):
        if t[cont2] - t[cont] <= tem:
            r += 1
        else:
            break
    if r > rmax:
        rmax = r

print(rmax)
