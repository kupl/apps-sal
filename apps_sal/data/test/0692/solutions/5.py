from fractions import gcd
n, m, r = int(input()), list(map(int, input().split())), list(map(int, input().split()))
lcm = m[0]
for mi in m:
    lcm = lcm * mi // gcd(lcm, mi)
print(sum(any(i % mj == rj for mj, rj in zip(m, r)) for i in range(lcm)) / lcm)
