(a, b) = list(map(int, input().split()))
c = 0
ans = 0
while a > 0:
    ans += a
    c += a
    a = c // b
    c %= b
print(ans)
