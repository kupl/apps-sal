n = int(input())
l = list(map(int, input().split()))
ans = 0
i = 0
mx = 0
while i < n:
    mx = max(mx, l[i])
    if i == mx - 1:
        ans += 1
    i += 1
print(ans)
