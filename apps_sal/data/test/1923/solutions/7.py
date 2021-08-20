N = int(input().strip())
L = list(map(int, input().strip().split()))
L.sort()
amt = 0
while len(L) > 0:
    (L1, L2) = L[0:2]
    amt += min([L1, L2])
    del L[0:2]
print(amt)
