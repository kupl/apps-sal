from decimal import Decimal, ROUND_CEILING

N = int(input())
pairs = (map(Decimal, input().split()) for _ in range(N))

t = Decimal('1')
a = Decimal('1')
def ceil(d): return d.to_integral_exact(rounding=ROUND_CEILING)


for ti, ai in pairs:
    mul = max(ceil(t / ti), ceil(a / ai))
    t = ti * mul
    a = ai * mul

print(int(t + a))
