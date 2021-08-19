(a, b) = map(int, input().split())
ans = 0
while True:
    if a < 2 and b < 2 or a < 1 or b < 1:
        break
    if a > b:
        a -= 2
        b -= 1
    else:
        a -= 1
        b -= 2
    ans += 1
print(ans)
