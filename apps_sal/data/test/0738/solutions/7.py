(a, b, c, d) = map(int, input().split())
sol = 0
z = c
sm = min(c - b, b - a)
bg = max(c - b, b - a)
while b + c >= z and z <= d:
    mn = a + b
    m1 = mn + sm
    mx = b + c
    m2 = mx - sm
    maxi = (sm + 1) * (bg + 1)
    if mn > z:
        sol += maxi
    if mn <= z and m1 > z:
        foo = z + 1 - mn
        sol += maxi
        sol -= foo * (foo + 1) // 2
    if m1 <= z and m2 > z:
        foo = sm * (sm + 1)
        foo //= 2
        maxi -= foo
        foo = z + 1 - m1
        maxi -= (sm + 1) * foo
        sol += maxi
    if m2 <= z and mx > z:
        foo = mx - z
        sol += foo * (foo + 1) // 2
    z += 1
print(sol)
