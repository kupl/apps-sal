import collections

N = int(input())
As = sorted(list(map(int, input().split())))
c = collections.Counter(As)

L = [0] * (10 ** 5 + 1)
M = [0] * (10 ** 5 + 1)
for (x, y) in list(c.items()):
    L[x] = y

for i in range(0, (10 ** 5)):
    M[i] = L[i - 1] + L[i] + L[i + 1]

print((max(M)))

