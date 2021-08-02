n, k = list(map(int, input().split()))
A = sorted(map(int, input().split()), reverse=True)

cnt = [0 for _ in range(100)]
max_a = A[0]
k += 1
index_k = 0
index_a = 0

for i in range(100):
    tmp = 2 ** i

    if tmp > max_a:
        index_a = i - 1
        break

    for a in A:
        if a < tmp:
            break
        if (a >> i) & 1:
            cnt[i] += 1

for i in range(100):
    tmp = 2 ** i

    if tmp > k:
        index_k = i - 1
        break

best = [0, ]

for i, c in enumerate(cnt[: index_k + 1]):

    best.append(best[-1] + max(c, n - c) * 2 ** i)

initial = 0

if index_a > index_k:

    initial = sum([2 ** x[0] * x[1] for x in enumerate(cnt[index_k + 1: index_a + 1], index_k + 1)])


equal = [initial, ]

for i, c in enumerate(cnt[index_k::-1]):

    if k >> (index_k - i) & 1:
        equal.append(equal[-1] + (n - c) * 2 ** (index_k - i))
    else:
        equal.append(equal[-1] + c * 2 ** (index_k - i))

ans = 0

for i in range(index_k + 1):

    if (k >> i) & 1:
        ans = max(ans, best[i] + cnt[i] * 2 ** i + equal[-(i + 2)])

print(ans)
