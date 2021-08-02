n, m = list(map(int, input().split()))
a = ([[0, 1], [0, m], [0, 0], [0, m - 1]], [[1, 0], [n, 0], [0, 0], [n - 1, 0]],
     [[0, 1], [n, m], [0, 0], [n, m - 1]], [[1, 0], [n, m], [0, 0], [n - 1, m]],
     [[0, 0], [n, m], [0, m], [n, 0]], [[0, 0], [n, m], [n, 0], [0, m]])
for x in max(a, key=lambda a: (len(set(map(tuple, a))) == len(a)) * all(map((lambda x: min(x[1], x[0]) >= 0), a)) * sum(((a[i][0] - a[i + 1][0]) ** 2 + (a[i][1] - a[i + 1][1]) ** 2) ** 0.5 for i in range(len(a) - 1))):
    print(*x)
print()
