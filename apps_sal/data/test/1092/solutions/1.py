MOD = 10 ** 9 + 7
fact = [1]
rfact = [1]
p2 = [1]

for i in range(1, 1010):
    fact.append((fact[-1] * i) % MOD)
    rfact.append((rfact[-1] * pow(i, MOD - 2, MOD)) % MOD)
    p2.append((p2[-1] * 2) % MOD)


def C(n, k):
    return (fact[n] * rfact[k] * rfact[n - k]) % MOD


n, m = list(map(int, input().split()))
pos = sorted(list(map(int, input().split()))) + [n + 1]

last = 1
ans = 1
n -= m
for x in pos:
    v = x - last
    ans = (ans * C(n, v)) % MOD
    if last > 1 and x < pos[-1] and v > 0:
        ans = (ans * p2[v - 1]) % MOD
    last = x + 1
    n -= v

print(ans)
