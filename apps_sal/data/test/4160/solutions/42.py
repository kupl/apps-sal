X = int(input())
cur = 100
ans = 0
while cur < X:
    cur = cur * 101 // 100
    ans += 1
print(ans)
