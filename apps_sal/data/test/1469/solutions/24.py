L = int(input())
n = len(str(bin(L))) - 3
e = []
for i in range(n):
    e.append((i + 1, i + 2, 0))
    e.append((i + 1, i + 2, 2**(n - i - 1)))
h = 2**n
for i, c in enumerate(str(bin((L)))[2:]):
    if c == "1" and i:
        e.append((1, i + 1, h))
        h += 2**(n - i)
print(n + 1, len(e))
for i in e:
    print(*i)
