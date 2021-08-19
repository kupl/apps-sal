import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
l = []
for i in range(1, n + 1):
    l.append(i)
m = []
for j in itertools.permutations(l, n):
    m.append(list(j))
for a in range(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2):
    if p == m[a]:
        x = a
        break
for b in range(9 * 8 * 7 * 6 * 5 * 4 * 3 * 2):
    if q == m[b]:
        y = b
        break
print(abs(x - y))
