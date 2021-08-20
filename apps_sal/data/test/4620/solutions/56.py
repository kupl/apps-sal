N = int(input())
C = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N - 1):
    (c, s, f) = C[i]
    A = s + c
    for j in range(i + 1, N - 1):
        (nc, ns, nf) = C[j]
        if A < ns:
            A = ns
        elif (A - ns) % nf != 0:
            A += nf - (A - ns) % nf
        A += nc
    print(A)
print(0)
