N, M = list(map(int, input().split()))
X = sorted(list(map(int, input().split())))
kyori = []

for i in range(M - 1):
    kyori.append(X[i + 1] - X[i])

# print(sorted(kyori)[:-N+1])

if N == 1:
    print((sum(kyori)))
else:
    print((sum(sorted(kyori)[:-N + 1])))
