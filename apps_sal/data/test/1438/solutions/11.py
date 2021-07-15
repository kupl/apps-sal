n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

kol = [b[i] // a[i] for i in range(n)]
ost = [b[i] % a[i] for i in range(n)]

ans = min(kol)

check = True
while check:
    check = False
    for i in range(n):
        if kol[i] == ans:
            if k >= a[i] - ost[i]:
                k -= a[i] - ost[i]
                ost[i] = 0
                kol[i] += 1
                check = True

    if check:
        ans = min(kol)

print(ans)
