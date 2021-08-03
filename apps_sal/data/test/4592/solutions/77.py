def bunkai(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


n = int(input())
s = [0] * (n + 1)
for i in range(1, n + 1):
    fact = bunkai(i)
    for j in fact:
        s[j] += 1
ans = 1

for i in range(0, n + 1):
    ans *= (s[i] + 1)
    ans %= 10**9 + 7

print(ans)
