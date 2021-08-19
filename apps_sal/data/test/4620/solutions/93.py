n = int(input())
csf = [tuple(map(int, input().split())) for _ in range(n - 1)]

for i in range(n - 1):
    c, s, f = csf[i]
    a = s + c
    now = i
    for j in range(i + 1, n - 1):
        nc, ns, nf = csf[j]
        # next = ns + nf * x
        if a <= ns:
            a = ns
        else:
            x = (a - ns + nf - 1) // nf
            a = ns + nf * x
        a += nc

    print(a)
print((0))
