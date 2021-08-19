n = int(input())
cur = 1
ans = 0
while n > 0:
    n -= cur
    cur *= 2
    ans += 1
print(ans)
