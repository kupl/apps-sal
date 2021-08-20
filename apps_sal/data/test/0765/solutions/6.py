(t, s, q) = list(map(int, input().split()))
ans = 1
while True:
    x = s * q
    if x >= t:
        break
    ans += 1
    s = x
print(ans)
