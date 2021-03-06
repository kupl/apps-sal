from bisect import bisect_left
n = int(input())
a = [0] * n
for i in range(n):
    (c, p) = map(int, input().split())
    a[i] = (p, c, i + 1)
a.sort(reverse=True)
m = int(input())
b = [0] * m
for (j, r) in enumerate(map(int, input().split())):
    b[j] = (r, j + 1)
b.sort()
(s, q) = (0, [])
for (p, c, i) in a:
    k = bisect_left(b, (c, 0))
    if k == len(b):
        continue
    (r, j) = b.pop(k)
    q.append(str(i) + ' ' + str(j))
    s += p
    if not b:
        break
print(len(q), s)
print('\n'.join(q))
