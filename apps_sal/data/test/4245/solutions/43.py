a, b = list(map(int, input().split()))
cnt = 1
ans = 0
while cnt < b:
    cnt += (a - 1)
    ans += 1
print(ans)
