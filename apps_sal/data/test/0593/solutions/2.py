n, m = [int(i) for i in input().split()]
a = []
b = [0] * n
for i in range(m):
    a.append([int(j) for j in input().split()])
    k = 0
    for j in range(1, n):
        if a[-1][j] > a[-1][k]:
            k = j
    a[-1] = k
    b[k] += 1
q = max(b)
for i in range(n):
    if b[i] == q:
        print(i + 1)
        return

