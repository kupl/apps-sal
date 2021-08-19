import collections
(N, X, Y) = [int(x) for x in input().split()]
c = collections.Counter()
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i == X and j == Y or (i == Y and j == X):
            c[1] += 1
        else:
            c[min([j - i, abs(X - i) + 1 + abs(Y - j), abs(X - j) + 1 + abs(Y - i)])] += 1
for i in range(1, N):
    print(c[i])
