N, M, X, *A = map(int, open(0).read().split())

l = [0] * N
for a in A:
    l[a - 1] = 1

print(min(sum(l[:X]), sum(l[X:])))
