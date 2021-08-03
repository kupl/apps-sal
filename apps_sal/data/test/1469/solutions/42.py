L = int(input())

N = L.bit_length()

E = []
for i in range(1, N):
    E.append((i, i + 1, 0))
    E.append((i, i + 1, 2 ** (i - 1)))

s = 2 ** (N - 1)
for i in reversed(list(range(N - 1))):
    if (L >> i) & 1:
        E.append((i + 1, N, s))
        s += 2 ** i

print((N, len(E)))
for a, b, c in E:
    print((a, b, c))
