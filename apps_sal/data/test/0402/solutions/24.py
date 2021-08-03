n, k = list(map(int, input().split()))
t = 240 - k
cur = 0
ans = 0
for i in range(1, n + 1):
    cur += i * 5
    if (cur > t):
        break
    ans += 1
print(ans)
