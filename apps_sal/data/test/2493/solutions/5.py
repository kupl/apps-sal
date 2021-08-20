from collections import Counter
N = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
up = [1 for i in range(N + 1)]
for i in range(2, N + 1):
    up[i] = up[i - 1] * i % mod
down = [1 for i in range(N + 1)]
down[N] = pow(up[N], mod - 2, mod)
for i in range(N - 1, 0, -1):
    down[i] = (i + 1) * down[i + 1] % mod


def ncr(n, r):
    if not n >= r >= 0:
        return 0
    else:
        return up[n] * down[n - r] * down[r] % mod


(duplicated_number, _cnt) = Counter(a).most_common()[0]
index_que = []
for i in range(N + 1):
    if a[i] == duplicated_number:
        index_que.append(i)
(A, B) = (min(index_que), max(index_que))
for k in range(1, N + 2):
    if k == 1:
        print(N)
    else:
        ans = ncr(N - 1, k - 2) + ncr(N - 1, k) + 2 * ncr(N - 1, k - 1) - ncr(N - B + A, k - 1)
        print(ans % mod)
