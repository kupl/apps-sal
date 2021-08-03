N, D = map(int, input().split())
X_list = []
Y_list = []
count = 0

for i in range(N):
    X, Y = map(int, input().split())
    X_list.append(X)
    Y_list.append(Y)

for i in range(N):
    if (X_list[i] ** 2) + (Y_list[i] ** 2) <= D ** 2:
        count += 1

print(count)
