def read():
    return list(map(int, input().split()))


n = int(input())
a = list(read())
ans = sum(a)
if ans % 2:
    Min = 10 ** 10
    for i in range(n):
        if a[i] % 2 and a[i] < Min:
            Min = a[i]
    if Min < 10 ** 10:
        ans -= Min
    else:
        ans = 0
print(ans)
