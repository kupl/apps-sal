from collections import Counter
H, W, N, *L = map(int, open(0).read().split())
dic = {}
for a, b in zip(*[iter(L)] * 2):
    for i in range(a - 2, a + 1):
        for j in range(b - 2, b + 1):
            if 0 < i and i + 2 <= H and 0 < j and j + 2 <= W:
                dic[i * W + j] = dic.get(i * W + j, 0) + 1
c = Counter(dic.values())
ans = [(H - 2) * (W - 2)] + [0] * 9
for k in c.keys():
    ans[k] = c[k]
    ans[0] -= c[k]
print('\n'.join(map(str, ans)))
