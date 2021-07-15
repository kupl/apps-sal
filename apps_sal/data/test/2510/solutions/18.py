from collections import Counter

N, M = map(int, input().split())
AB = [map(int, input().split()) for _ in range(M)]

F = list(range(N+1))
for A, B in AB:
    H = []
    while F[A] != A:
        H.append(A)
        A = F[A]
    while F[B] != B:
        H.append(B)
        B = F[B]
    for h in H+[B]:
        F[h] = A

for i, f in enumerate(F):
    H = [i]
    while F[f] != f:
        H.append(f)
        f = F[f]
    for h in H:
        F[h] = f

print(Counter(F).most_common(1)[0][1])
