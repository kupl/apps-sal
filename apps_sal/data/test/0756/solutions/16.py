n = int(input())
a = list(map(int, input().split()))
ans = 0
check = False
for i in range(n):
    if a[i] - ans > 15:
        ans += 15
        check = True
        break
    else:
        ans = a[i]
if not check:
    if 90 - ans <= 15:
        ans = 90
    else:
        ans += 15
print(ans)
