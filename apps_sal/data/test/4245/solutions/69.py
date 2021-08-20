(a, b) = map(int, input().split())
free = 1
ans = 0
while free < b:
    free += a - 1
    ans += 1
print(ans)
