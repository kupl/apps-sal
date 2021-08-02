n = int(input())
A = [int(i) for i in input().split()]

X = [[] for i in range(n + 1)]

for i, a in enumerate(A):
    X[a].append(i)

Sasha = 0
Dima = 0
ans = 0
for i in range(1, n + 1):
    d1 = abs(Sasha - X[i][0]) + abs(Dima - X[i][1])
    d2 = abs(Sasha - X[i][1]) + abs(Dima - X[i][0])
    if d1 < d2:
        ans += d1
        Sasha = X[i][0]
        Dima = X[i][1]
    else:
        ans += d2
        Sasha = X[i][1]
        Dima = X[i][0]

print(ans)
