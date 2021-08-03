def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
total = 1
ans = 1
inf = 10**9 + 7
total = [0] * 1000
for i in range(1, N + 1):
    temp = prime_factorize(i)
    for j in range(len(temp)):
        total[temp[j] - 1] += 1


for i in range(1000):
    ans *= total[i] + 1
    ans %= inf
print(ans)
