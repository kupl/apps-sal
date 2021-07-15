def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b
n, t = int(input()), list(map(int, input().split()))
j = t[0]
for i in t[1: ]: j = gcd(i, j)
print(n * j)
