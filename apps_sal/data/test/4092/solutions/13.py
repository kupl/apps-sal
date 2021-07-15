n = int(input())
a = list(map(int, input().split()))
m = {0}
ans = 0
summ = 0
for i in range(n):
    summ += a[i]
    if summ == 0 or summ in m:
        ans += 1
        m = {a[i]}
        summ = a[i]
    else:
        m.add(summ)
print(ans)

