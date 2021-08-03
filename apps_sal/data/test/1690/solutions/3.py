n = int(input())
a = list(map(int, input().split()))
ans = 0
mx = a[-1] + 1
for i in range(n - 1, -1, -1):
    ans += max(0, min(mx - 1, a[i]))
    mx = min(mx - 1, a[i])
print(ans)
