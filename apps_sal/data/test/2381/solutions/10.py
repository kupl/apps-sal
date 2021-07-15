N, K = list(map(int, input().split()))
A = tuple(map(int, input().split()))
MOD = 10 ** 9 + 7

if K == N:
    ans = 1
    for x in A:
        ans = (ans * x) % MOD
    print(ans)
    return

plus, minus = [], []
for a in A:
    if a >= 0:
        plus.append(a)
    else:
        minus.append(a)

plus.sort(reverse=True)
minus.sort()

if not plus:
    ans = 1
    if K % 2:
        # 答えは負値になるので絶対値小さいのを取る
        for x in minus[-K:]:
            ans = (ans * x) % MOD
    else:
        # 答えは非負値になるので絶対値大きいのを取る
        for x in minus[:K]:
            ans = (ans * x) % MOD
    print(ans)
    return

idx = 0
for i in range(2, N, 2):
    if K - i < 0:
        break
    if not len(plus) >= K - i + 2:
        idx += 2
        continue
    if len(minus) >= i:
        if minus[i - 2] * minus[i - 1] < plus[K - i + 1] * plus[K - i]:
            break
        else:
            idx += 2

ans = 1
for x in minus[:idx] + plus[:K - idx]:
    ans = (ans * x) % MOD
print(ans)

