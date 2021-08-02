N, M = map(int, input().split())
D = []
E = []
if M % 2 == 0:
    if N % 2 == 0:
        N -= 1
    a = (N + 1) // 2
    for i in range(a // 2):
        D.append((i + 1, a - i))
    for d, e in D:
        E.append((d + a, e + a - 1))
else:
    if N % 2 == 0:
        N -= 1
    a = N // 2
    for i in range(a // 2):
        D.append((i + 1, a - i))
    for d, e in D:
        E.append((d + a + 1, e + a))
    E.append((a + 1, N))
F = D + E
for i in range(M):
    print(*F[i])
