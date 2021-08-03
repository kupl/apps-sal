n = int(input())
L = []
for i in range(n):
    L.append(list(map(int, input().split())) + [i + 1])
# print(L)
L.sort(key=lambda X: (X[0], -X[1], X[2]))
# print(L)
X = 0
for i in range(1, n):
    if L[i][1] <= L[i - 1][1]:
        print(L[i][2], L[i - 1][2])
        X = 1
        break
if X == 0:
    print(-1, -1)
