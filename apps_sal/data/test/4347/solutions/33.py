def ncr(n, r):
    return fact[n] // (fact[r] * fact[n - r])


n = int(input())
fact = [1 for i in range(25)]
for i in range(2, 25):
    fact[i] = fact[i - 1] * i
if n == 2:
    print(1)
    quit()
if n == 4:
    print(3)
    quit()
z = ncr(n, n // 2) // 2
z = z * (fact[n // 2 - 1] * fact[n // 2 - 1])
print(z)
