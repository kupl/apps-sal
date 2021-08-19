(a, b) = map(int, input().split())
ans = 0
while 1 + (a - 1) * ans < b:
    ans += 1
print(ans)
