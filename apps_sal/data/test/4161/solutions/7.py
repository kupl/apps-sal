from math import gcd
K = int(input())
print(sum(gcd(a + 1, gcd(b + 1, c + 1))for a in range(K)for b in range(K)for c in range(K)))
