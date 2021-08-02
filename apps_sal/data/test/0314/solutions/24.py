n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
a1, a2 = 0, 0
ans = False

for i in range(n):
    a1 += a[i]
    a2 += min(8, a1)
    a1 -= min(8, a1)
    if a2 >= k:
        ans = i + 1
        break

if ans:
    print(ans)
else:
    print(-1)
