from collections import defaultdict

s = input()
l = defaultdict(int)
for c in s:
    l[c] += 1

u = sorted(list(filter(lambda x: l[x] % 2, l.keys())))

for i in range(0, int(len(u) / 2)):
    l[u[i]] += 1
    l[u[-i-1]] -= 1

r = ""
for c in sorted(l.keys()):
    r += c * int(l[c] / 2)

c = u[int(len(u) / 2)] if len(u) % 2 else ""

print(r + c + r[::-1])
