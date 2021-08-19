(H, W) = map(int, input().split())
L = []
for i in range(H):
    C = list(map(str, input().split()))
    L.append(C)
    L.append(C)
for i in range(2 * H):
    print(L[i][0])
