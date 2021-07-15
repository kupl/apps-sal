N = int(input())
*B, = map(int, input().split())
C = [0]*64
L = [[] for i in range(64)]
for b in B:
    l = (b & -b).bit_length()
    C[l] += 1
    L[l].append(b)
i = C.index(max(C))
R = [b for b in B if (b & -b).bit_length() != i]
print(len(R))
if R:
    print(*R)
