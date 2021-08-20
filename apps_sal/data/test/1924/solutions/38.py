m = 1000000007
(r1, c1, r2, c2) = map(int, input().split())
nf = 10 ** 6 * 2 + 100
fact = [0] * (nf + 1)
fact[0] = 1
for i in range(nf):
    fact[i + 1] = fact[i] * (i + 1) % m


def F(r, c):
    path = fact[r + c + 2] % m * pow(fact[r + 1] * fact[c + 1], m - 2, m) % m
    return path - 1


r1 -= 1
c1 -= 1
ans = F(r2, c2)
ans -= F(r1, c2)
ans -= F(r2, c1)
ans += F(r1, c1)
ans = ans % m
print(ans)
