from itertools import product
(N, *ABC) = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))
ans = 10 ** 9
for X in product((0, 1, 2, 3), repeat=N):
    (cnt, K, temp) = ([0] * 4, [0] * 4, 0)
    for i in range(N):
        cnt[X[i]] += 1
        K[X[i]] += L[i]
    if min(cnt[1:]) == 0:
        continue
    for i in range(3):
        temp += abs(ABC[i] - K[i + 1])
        temp += 10 * max(cnt[i + 1] - 1, 0)
    ans = min(ans, temp)
print(ans)
