(a, b) = map(int, input().split())
ans = 0
if a >= b:
    ans += a
    a -= 1
    if a >= b:
        ans += a
    else:
        ans += b
else:
    ans += b
    b -= 1
    if b >= a:
        ans += b
    else:
        ans += a
print(ans)
