
n = int(input())
mod = 10**9 + 7

is_prime = [True for _ in range(1100)]
is_prime[0] = is_prime[1] = False
for i in range(2, 1100):
    if not is_prime[i]:
        continue
    for j in range(i * i, 1100, i):
        is_prime[j] = False

ind = []

for p in range(2, 1100):
    if is_prime[p]:
        cnt = 0
        for m in range(2, n + 1):
            while m % p == 0:
                m //= p
                cnt += 1
        if cnt != 0:
            ind.append(cnt)

ans = 1
for i in range(len(ind)):
    ans *= (ind[i] + 1)

print((ans % mod))
