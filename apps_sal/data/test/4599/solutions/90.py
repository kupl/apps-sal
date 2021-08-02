n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 2:
        ans -= a[i]
    else:
        ans += a[i]
print(ans)
