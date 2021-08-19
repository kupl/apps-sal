import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = []
for i in range(1, n + 1):
    a.append(i)
b = []
for v in itertools.permutations(a, n):
    b.append(v)
x = 0
for j in b:
    if list(j) == p:
        x = b.index(j)
y = 0
for k in b:
    if list(k) == q:
        y = b.index(k)
print(abs(x - y))
