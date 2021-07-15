N, M = [int(x) for x in input().split()]
C = [0 for _ in range(N)]
V = []
IDs = []
for i in range(M):
    P, Y = [int(x) for x in input().split()]
    V.append([Y, P, i])
V.sort()
for v in V:
    C[v[1] - 1] += 1
    x = C[v[1] - 1]
    IDs.append(f"{v[2]:06d}{v[1]:06d}{x:06d}")
IDs.sort()
for i in IDs:
    print((i[6:]))

