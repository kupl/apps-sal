n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -= a[i]
print(ans)
