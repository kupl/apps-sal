import fractions
c = 0
N = int(input())
L = list(map(int, input().split()))
a = L[0]
for i in range(1, N):
    a = L[i] * a // fractions.gcd(L[i], a)
for i in range(N):
    c += a // L[i]
print(c % (10 ** 9 + 7))
