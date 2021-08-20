(k, a, b, v) = map(int, input().split())
ans = 0
while a > 0:
    ans += 1
    kn = min(k, b + 1)
    a -= v * kn
    b = max(b - k + 1, 0)
print(ans)
