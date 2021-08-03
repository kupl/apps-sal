import itertools


L = [int(input()) for _ in range(5)]
K = int(input())
Lcombi = itertools.combinations(L, 2)

for lc in Lcombi:
    if abs(lc[0] - lc[1]) > K:
        print(":(")
        return

print("Yay!")
