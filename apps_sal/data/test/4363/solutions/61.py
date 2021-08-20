(k, s) = map(int, input().split())
ans = 0
for i in range(k + 1):
    num = s - i
    for j in range(min(num + 1, k + 1)):
        if 0 <= num - j <= k:
            ans += 1
print(ans)
