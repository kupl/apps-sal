MOD = (int)(1e9 + 7)


def power(a, n):
    if a == 0: return 0
    if n == 0: return 1

    res = 1
    while n > 0:
        if n % 2 == 1: res = res * a % MOD
        a = a * a % MOD
        n //= 2

    return res


def inverse(n):
    return power(n, MOD - 2)


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

B = []
pos, neg = 0, 0
for a in A:
    if a > 0:
        B.append([a, 1])
        pos += 1
    if a < 0:
        B.append([-a, -1])
        neg += 1
    if a == 0:
        B.append([0, 0])
B.sort(reverse=True)

ans, sign = 1, 1
if N == neg and K % 2 == 1:
    for i in range(K):
        ans *= B[N - 1 - i][0]
        ans %= MOD
    print((-ans % MOD))
    return

for i in range(K):
    ans *= B[i][0]
    ans %= MOD
    sign *= B[i][1]

if N == K:
    if sign >= 0: print(ans)
    else: print((-ans % MOD))
    return

if sign < 0:
    out_neg, out_pos = 0, 0
    in_pos, in_neg = 0, 0

    for i in range(K):
        if B[K - 1 - i][1] < 0:
            out_neg = B[K - 1 - i][0]
            break

    for i in range(K):
        if B[K - 1 - i][1] > 0:
            out_pos = B[K - 1 - i][0]
            break

    for i in range(N - K):
        if B[K + i][1] > 0:
            in_pos = B[K + i][0]
            break

    for i in range(N - K):
        if B[K + i][1] < 0:
            in_neg = B[K + i][0]
            break

    if in_neg == 0 or out_pos == 0:
        ans = (ans * in_pos % MOD) * inverse(out_neg) % MOD
    elif in_pos == 0 or out_neg == 0:
        ans = (ans * in_neg % MOD) * inverse(out_pos) % MOD
    else:
        if out_pos * in_pos < out_neg * in_neg:
            ans = (ans * in_neg % MOD) * inverse(out_pos) % MOD
        else:
            ans = (ans * in_pos % MOD) * inverse(out_neg) % MOD

print(ans)
