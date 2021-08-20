(n, m) = list(map(int, input().split()))
(mod1, mod2, mod3, mod4, mod5) = (n // 5, n // 5, n // 5, n // 5, n // 5)
if n % 5 >= 1:
    mod1 += 1
if n % 5 >= 2:
    mod2 += 1
if n % 5 >= 3:
    mod3 += 1
if n % 5 == 4:
    mod4 += 1
(m1, m2, m3, m4, m5) = (m // 5, m // 5, m // 5, m // 5, m // 5)
if m % 5 >= 1:
    m1 += 1
if m % 5 >= 2:
    m2 += 1
if m % 5 >= 3:
    m3 += 1
if m % 5 == 4:
    m4 += 1
print(mod1 * m4 + mod2 * m3 + mod3 * m2 + mod4 * m1 + mod5 * m5)
