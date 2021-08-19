(N, M, *A) = map(int, open(0).read().split())
c = 0
for (a, b) in sorted(zip(*[iter(A)] * 2))[::-1]:
    if b <= N:
        c += 1
        N = a
print(c)
