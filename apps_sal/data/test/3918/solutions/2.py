n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
while k1 + k2 > 0:
    max_dif = -10000000000000
    ind = -1    
    for i in range(n):
        if (a[i] - b[i]) ** 2 > max_dif:
            max_dif = (a[i] - b[i]) ** 2
            ind = i
    if k1 != 0:
        k1 -= 1
        if a[ind] > b[ind]:
            a[ind] -= 1
        else:
            a[ind] += 1
    elif k2 != 0:
        k2 -= 1
        if b[ind] > a[ind]:
            b[ind] -= 1
        else:
            b[ind] += 1
ans = 0
for i in range(n):
    ans += (a[i] - b[i]) ** 2
print(ans)
