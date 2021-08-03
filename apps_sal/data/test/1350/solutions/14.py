n, k = map(int, input().split())
s = input()
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:k]
d = dict()
for u in upper:
    d[u] = 0
for l in s:
    d[l] += 1

print(min(d.values()) * k)
