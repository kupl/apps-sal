from collections import defaultdict


def comb(n, r):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    res = 1
    for i in range(r):
        res *= n
        n -= 1
    for i in range(1, r + 1):
        res //= i
    return res


N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))
V.sort(reverse=True)
mi = 10**18
dic = defaultdict(int)
dic2 = defaultdict(int)
tot = 0
for i, a in enumerate(V):
    if i < A:
        tot += a
        dic2[a] += 1
        if a < mi:
            mi = a
    dic[a] += 1
if len(dic2) == 1:
    ans = 0
    for i in range(A, B + 1):
        ans += comb(dic[mi], i)
else:
    ans = comb(dic[mi], dic2[mi])
print((tot / A))
print(ans)
