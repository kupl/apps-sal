from itertools import dropwhile
l = int(input())
k = [(l >> i & 1) for i in range(20)][::-1]
k = list(dropwhile(lambda x: x == 0, k))
n = len(k)
path = []
for i in range(n - 1):
    path.append((i + 1, i + 2, 0))
    path.append((i + 1, i + 2, 2**i))

path_len = 2**(n - 1)
for i in range(1, n):
    if k[i]:
        x = n - 1 - i
        path.append((x + 1, n, path_len))
        path_len += (2**x)

m = len(path)
print(n, m)
for i in path:
    print(i[0], i[1], i[2])
