n = int(input())
A = [int(x) for x in input().split()]
P = [0]
for a in A:
    P.append(P[-1] + a)
mn = min(P)
P = [p - mn + 1 for p in P]
if set(range(1, n + 1)) == set(P):
    print(*P)
else:
    print(-1)
