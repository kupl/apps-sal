N = int(input())
D = {}
L = list(map(int, input().split()))[::-1]
for i in L:
    D[i] = max(D.get(i, 0), D.get(i + 1, 0) + 1)
M = max([(i[1], -i[0]) for i in D.items()])
L.reverse()
print(M[0])
M = -M[1]
for i in range(N):
    if L[i] == M:
        print(i + 1, end=' ')
        M += 1
