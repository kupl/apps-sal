(t, s, q) = map(int, input().split())
x = s
ans = 1
while x < t:
    ans += 1
    x += (q - 1) * s
    s = x
print(ans - 1)
