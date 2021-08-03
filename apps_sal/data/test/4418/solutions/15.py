n = int(input())
x = [4, 8, 15, 16, 23, 42]
r = [0] * len(x)
z = 0
for v in map(int, input().split()):
    i = x.index(v)
    if not i or r[i - 1] > r[i]:
        r[i] += 1
    else:
        z += 1
z += sum(v - r[-1] for v in r)
print(z)
