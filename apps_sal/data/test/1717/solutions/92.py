from fractions import gcd

n = int(input())
kotae = 1
for i in range(2, n + 1):
    kotae = kotae * i // gcd(kotae, i)
print((kotae + 1))
