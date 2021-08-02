import itertools

n = int(input())
d = {'M': 0, 'A': 1, 'R': 2, 'C': 3, 'H': 4}
h = [0, 0, 0, 0, 0]
for _ in range(n):
    name = input()
    if name[0] in d.keys():
        h[d[name[0]]] += 1

ans = 0
for i, j, k in itertools.combinations([0, 1, 2, 3, 4], 3):
    ans += h[i] * h[j] * h[k]
print(ans)
