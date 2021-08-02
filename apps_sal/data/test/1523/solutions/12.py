n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [0] * k
d = []
for (ai, bi) in zip(a, b):
    if(c[ai - 1] != 0):
        d.append(min(c[ai - 1], bi))
    else:
        k -= 1
    c[ai - 1] = max(c[ai - 1], bi)
d.sort()
print(sum(d[:k]))
