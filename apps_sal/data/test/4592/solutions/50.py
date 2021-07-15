MOD = 10 ** 9 + 7
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
n = int(input())
cnt = [0]*10000
sum = []
for i in range(2, n + 1):
    sum += prime_factorize(i)

for x in sum:
    cnt[x] += 1
ans = 1
for i in range(len(cnt)):
    if cnt[i] > 0:
        ans *= (cnt[i]+1)
print(ans % MOD)
