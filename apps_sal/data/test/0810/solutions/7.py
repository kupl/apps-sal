a, b, n = list(map(int, input().split()))
m = 1000000007
fact = [1]

for i in range(1, n + 1):
    fact.append((fact[-1] * i) % m)
ans = 0
for i in range(n + 1):
    su = (a * i) + b * (n - i)
    coef = 1
    while(su > 0):
        if(su % 10 != a and su % 10 != b):
            coef = 0
        su //= 10
    if coef:
        ans += (fact[n] * pow((fact[i] * fact[n - i]), m - 2, m))
        ans = ans % m
print(ans % m)
