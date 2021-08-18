M = [0 for i in range(367)]
F = [0 for i in range(367)]
n = int(input())
for i in range(n):
    a, b, c = input().split()
    b = int(b)
    c = int(c)
    if a == 'M':
        for j in range(b, c + 1):
            M[j] += 1
    else:
        for j in range(b, c + 1):
            F[j] += 1

m = 0
for i in range(1, 367):
    x = min(M[i], F[i])
    if x > m:
        m = x
print(m * 2)
