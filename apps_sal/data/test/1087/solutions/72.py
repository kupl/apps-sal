(n, k) = list(map(int, input().split()))
A = sorted(map(int, input().split()), reverse=True)
cnt = [0 for _ in range(100)]
m = A[0]
for i in range(100):
    ten = 2 ** i
    if ten > m:
        break
    for a in A:
        if a < ten:
            break
        if a >> i & 1:
            cnt[i] += 1
for m in range(100):
    if 2 ** m > k + 1:
        j = m - 1
        break
initial = 0
if i > j:
    for (m, c) in enumerate(cnt[j + 1:i + 1], j + 1):
        initial += 2 ** m * c
best = [0]
for (m, c) in enumerate(cnt[:j + 1]):
    best.append(best[-1] + max(c, n - c) * 2 ** m)
K = list()
equal = [initial]
for (m, c) in enumerate(cnt[j::-1]):
    y = k + 1 >> j - m & 1
    K.append(y)
    if y == 1:
        equal.append(equal[-1] + (n - c) * 2 ** (j - m))
    else:
        equal.append(equal[-1] + c * 2 ** (j - m))
ans = 0
K.reverse()
for i in range(j + 1):
    if K[i]:
        ans = max(ans, best[i] + 2 ** i * cnt[i] + equal[-(i + 2)])
print(ans)
