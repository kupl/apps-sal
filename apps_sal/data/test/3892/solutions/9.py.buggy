n, m = list(map(int, input().split()))
ms, md = [n - 1 for i in range(n + 1)], [-1 for i in range(n + 1)]


def distance(sfrom, sto):
    nonlocal n
    return sto - sfrom if sto >= sfrom else sto + n - sfrom


for i in range(m):
    c, d = list(map(int, input().split()))
    md[c] += 1
    ms[c] = min(distance(c, d), ms[c])
for i in range(1, n + 1):
    md[i] = n * md[i] + ms[i]
ans = []
for i in range(1, n + 1):
    ans.append(max([md[k] + distance(i, k)if md[k] > 0 else 0 for k in range(1, n + 1)]))
print(' '.join([str(i)for i in ans]))
