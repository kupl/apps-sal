
import fractions


N = int(input())
a = []

for i in range(2, N + 1):
    a.append(i)

ans = a[0]

for i in range(1, N - 1):
    ans = ans * a[i] // fractions.gcd(ans, a[i])

print((ans + 1))

