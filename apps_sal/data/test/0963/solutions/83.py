mod = 998244353
n, k = map(int, input().split())
list_N = [0] * (n + 1)
list_N[1] = 1
list_N[2] = -1
d = []
for _ in range(k):
    l, r = map(int, input().split())
    d.append([l, r])
cnt = 0
for i in range(1, n + 1):
    cnt += list_N[i]
    cnt %= mod
    if cnt != 0:
        for l, r in d:
            if i + l <= n:
                list_N[i + l] += 1 * cnt
            if i + r + 1 <= n:
                list_N[i + r + 1] -= 1 * cnt

print(cnt % mod)
