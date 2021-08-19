# ABC115
# B Christmas Eve Eve
N = int(input())
P = []
for n in range(N):
    P.append(int(input()))
P = sorted(P, reverse=True)
print((sum(P) - P[0] // 2))
