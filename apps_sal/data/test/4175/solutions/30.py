N = int(input())
L = []
for _ in range(N):
    W = str(input())
    if W in L:
        print('No')
        return
    L.append(W)
for i in range(N - 1):
    if L[i][len(L[i]) - 1] != L[i + 1][0]:
        print('No')
        return
print('Yes')
