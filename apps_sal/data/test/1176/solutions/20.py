n = int(input())
a = list(map(int, input().split()))

ans = 0
count = 0
for i in range(n):
    if a[i] < 0:
        count += 1
    a[i] = abs(a[i])
    ans += a[i]
if count % 2 == 0:
    print(ans)
else:
    ans -= 2 * min(a)
    print(ans)
