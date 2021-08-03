a, b = map(int, input().split())
aki = 1
ans = 0
while aki < b:
    aki += a - 1
    ans += 1
print(ans)
