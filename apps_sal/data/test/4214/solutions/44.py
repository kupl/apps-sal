import itertools
n = int(input())
s = ''.join([str(_) for _ in range(n)])
l = list(itertools.permutations(s, n))
x = []
y = []
for i in range(n):
    (xi, yi) = map(int, input().split())
    x.append(xi)
    y.append(yi)
c = 0.0
for j in l:
    for k in range(n - 1):
        c += ((x[int(j[k])] - x[int(j[k + 1])]) ** 2 + (y[int(j[k])] - y[int(j[k + 1])]) ** 2) ** 0.5
print(c / len(l))
