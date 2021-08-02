n, m = [int(i) for i in input().split()]
f = [True] * (m + 1)
f[0] = False
for i in range(n):
    p, q = [int(j) for j in input().split()]
    for j in range(p, q + 1):
        f[j] = False
print(sum(f))
for i in range(1, m + 1):
    if f[i]:
        print(i, end=" ")
print()
