N = int(input())
d = 2
ans = 0
while d * d <= N:
    if N % d != 0:
        d += 1
        continue
    z = d
    while N % z == 0:
        N //= z
        z *= d
        ans += 1
    while N % d == 0:
        N //= d
if N != 1:
    ans += 1
print(ans)
