L = int(input())
N = len(str(bin(L))) - 3
E = []

for n in range(N):
    E.append((n + 1, n + 2, 0))
    E.append((n + 1, n + 2, 2**(N - n - 1)))

H = 2**N

for i, c in enumerate(str(bin((L)))[2:]):
    if c == "1" and i:
        E.append((1, i + 1, H))
        H += 2**(N - i)

print((N + 1, len(E)))
for e in E:
    print((*e))
