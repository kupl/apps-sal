(n, k) = map(int, input().split())
y = list(map(int, input().split()))
ans = 0
for a in y:
    if a <= 5 - k:
        ans += 1
print(ans // 3)
