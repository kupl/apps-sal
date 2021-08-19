(a, b) = map(int, input().split())
ans = 0
while True:
    a *= 3
    b *= 2
    ans += 1
    if a > b:
        break
print(ans)
