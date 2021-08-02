import collections
n, m = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

J = [0] * m
D = []
for i in range(m):
    D.append([])
x = n // m
s = 0
for i in range(m):
    D[i] = []
for i in range(n):
    J[L[i] % m] += 1
    D[L[i] % m].append(i)

Free = collections.deque([])
F = 0
for i in range(2 * m - 1):
    j = i % m
    if J[j] > x:
        t = J[j] - x
        F += t
        for A in range(t):
            Free.append((j, D[j][A]))
        J[j] = x
    elif J[j] < x:
        while (F > 0) and (J[j] < x):
            F -= 1
            J[j] += 1
            a, b = Free.popleft()
            s += (j - a) % m
            L[b] += (j - a) % m
print(s)
for i in L:
    print(i, end=' ')
