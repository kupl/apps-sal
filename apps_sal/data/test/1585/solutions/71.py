x, y = map(int, input().split())
ans = 0
cur = x
while cur <= y:
    ans += 1
    cur *= 2
print(ans)
