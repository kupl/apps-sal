(n, a, b) = list(map(int, input().split()))
c = [0]
for i in range(1, n + 1):
    c += [i]
for i in range(1, n + 1):
    c += [i]
for i in range(1, n + 1):
    c += [i]
print(c[a + n + b % n])
