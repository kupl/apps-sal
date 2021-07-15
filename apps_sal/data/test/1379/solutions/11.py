R = lambda: map(int, input().split())
n, m, d = R()
a = sorted((x, i) for i, x in enumerate(R()))
res = [-1] * len(a)
res[0] = 0
cnt = 0
l = 0
for r in range(1, n):
    if a[r][0] - d <= a[l][0]:
        cnt += 1
        res[r] = cnt
    else:
        res[r] = res[l]
        l += 1
print(max(res) + 1)
for t in sorted(zip(a, res), key=lambda x: x[0][1]):
    print(t[1] + 1, end=' ')
