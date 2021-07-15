from fractions import gcd
n, a, b, p, q = map(int, input().split())
k = (a*b)//gcd(a, b)
divisors_a = n//a
divisors_b = n//b
divisors_k = n//k
print(max((divisors_a - divisors_k)*p + divisors_b*q, (divisors_b - divisors_k)*q + divisors_a*p))
