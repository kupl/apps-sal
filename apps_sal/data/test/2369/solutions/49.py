def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return factorials, invs


n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


MOD = 10 ** 9 + 7
facts, invs = prepare(n, MOD)

ans_max = 0
for i in range(k - 1, n):
    ans_max += (arr[i] * facts[i] * invs[k - 1] * invs[i - k + 1]) % MOD

arr.sort(reverse=True)

ans_min = 0
for i in range(k - 1, n):
    ans_min += (arr[i] * facts[i] * invs[k - 1] * invs[i - k + 1]) % MOD

print((ans_max - ans_min) % MOD)
