a, b = map(int, input().split(' '))
ans = 0
if a == 1 and b == 1:
    print(0)
    return
while min(a, b) > 0:
    ans += 1
    if a > b:
        a -= 2
        b += 1
    else:
        b -= 2
        a += 1
print(ans)
