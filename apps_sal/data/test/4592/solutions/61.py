n = int(input())
is_prime = [True] * 1005
MOD = 10 ** 9 + 7
is_prime[0] = is_prime[1] = False
factors = []
for i in range(2, n + 1):
    if is_prime[i]:
        cnt = 0
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
        i_init = i
        while i <= n:
            cnt += n // i
            i *= i_init
        factors.append(cnt)
ans = 1
for x in factors:
    ans = ans * (x + 1) % MOD
print(ans)
