n = int(input())
a = list(map(int, input().split()))
mi = 0
ans = 0
o = 0
for i in range(n):
    if a[i] < 0:
        ans += -1 - a[i]
        mi += 1
    elif a[i] == 0:
        o += 1
        ans += 1
    else:
        ans += a[i] - 1
if mi % 2 == 1:
    if o == 0:
        ans += 2
print(ans)
