N = 2 * 10 ** 5 + 3
n = int(input())
(A, cnt) = (list(map(int, input().split(' '))), {})
(s, a) = (0, 0)
for i in range(n - 1, -1, -1):
    a += s
    if A[i] - 1 in cnt:
        a += cnt[A[i] - 1]
    if A[i] + 1 in cnt:
        a -= cnt[A[i] + 1]
    a -= (n - (i + 1)) * A[i]
    s += A[i]
    if A[i] not in cnt:
        cnt[A[i]] = 0
    cnt[A[i]] += 1
print(a)
