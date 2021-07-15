a, b = map(int, input().split())
ans = 0
while a + b > 2 and a > 0 and b > 0:
    ans += 1
    if a < b:
        a += 1
        b -= 2
    else:
        a -= 2
        b += 1
print(ans)
