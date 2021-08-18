N, *P = map(int, open(0).read().split())

A = []

cur = 1
for i in range(N):
    if P[i] == cur:
        A += reversed(range(cur, i + 1))
    elif P[i] != i + 2:
        if i + 1 == N or P[i + 1] != cur:
            print(-1)
            return
        A += reversed(range(cur, i + 2))
        P[i + 1] = P[i]
        cur = i + 2

for a in A:
    print(a)
