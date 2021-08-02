k, a, b = list(map(int, input().split()))
ans = 0
if b < 0:
    a *= -1
    b *= -1
    (b, a) = (a, b)
if a > 0 and b >= 0:
    ans += b // k - (a - 1) // k
else:
    ans += b // k
    ans += 1
    ans += (-a) // k

print(ans)
