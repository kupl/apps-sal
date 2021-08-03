n, m = map(int, input().split())
p = [0] * (m + 1)
for i in map(int, input().split()):
    p[i] += 1
r, q = [], sorted((p[i], i) for i in range(1, m + 1))
k = q[m - 1][0]
print(n - max(2 * k - n, 0))
for i in q:
    r.extend([str(i[1])] * i[0])
print('\n'.join(i + ' ' + j for i, j in zip(*(r, r[k:] + r[: k]))))
