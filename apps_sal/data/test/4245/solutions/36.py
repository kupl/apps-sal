a, b = map(int, input().split())
tmp = 1
ans = 0
while True:
    if tmp >= b:
        break
    tmp -= 1
    tmp += a
    ans += 1
print(ans)
