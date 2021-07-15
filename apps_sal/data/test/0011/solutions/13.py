def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

n, a, b, p, q = [int(i) for i in input().split()]
lcm = a * b // gcd(a,b)
onlyA = n//a - n//lcm
onlyB = n//b - n//lcm
print(p * onlyA + q * onlyB + max(p,q) * (n // lcm))

