(X, Y, N) = list(map(int, input().split()))
lst = [[0 for i in range(X)] for j in range(Y)]
for i in list(range(N)):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        for j in range(Y):
            for k in range(x):
                lst[j][k] = 1
    elif a == 2:
        for j in range(Y):
            for k in range(X - 1, x - 1, -1):
                lst[j][k] = 1
    elif a == 3:
        for j in range(y):
            for k in range(X):
                lst[j][k] = 1
    elif a == 4:
        for j in range(Y - 1, y - 1, -1):
            for k in range(X):
                lst[j][k] = 1
count = 0
for i in lst:
    count += i.count(0)
print(count)
