n = int(input())
cur = 0
ans = 0
while n - cur > 5:
    cur += 5
    ans += 1
print(ans + 1)
