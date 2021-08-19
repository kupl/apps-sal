import sys
input = sys.stdin.readline
(N, K) = map(int, input().split())
sushi = [tuple(map(int, input().split())) for _ in range(N)]
sushi.sort(key=lambda x: x[1], reverse=True)
used = [0 for _ in range(N)]
dup = []
deli = 0
for i in range(K):
    (t, d) = sushi[i]
    if used[t - 1]:
        dup.append(d)
    used[t - 1] = 1
    deli += d
vari = sum(used)
sat = vari ** 2 + deli
dup.sort(reverse=True)
for i in range(N - K):
    if not dup:
        break
    (t, d) = sushi[K + i]
    if used[t - 1]:
        continue
    used[t - 1] = 1
    deli -= dup.pop()
    deli += d
    vari += 1
    sat = max(sat, vari ** 2 + deli)
print(sat)
