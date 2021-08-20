import collections
n = int(input())
l = sorted(list(map(int, input().split())))
c = collections.Counter(l)
L = [0] * (10 ** 5 + 1)
M = [0] * (10 ** 5 + 1)
for (x, y) in c.items():
    L[x] += y
M[0] = L[0]
M[10 ** 5] = L[10 ** 5]
for i in range(1, 10 ** 5):
    M[i] = L[i - 1] + L[i] + L[i + 1]
print(max(M))
