K = int(input())
n = 1
dn = 1
c = 0
while c < K:
    print(n)
    c += 1
    if (n + dn) > sum(map(int, str(n + dn))) * dn:
        dn *= 10
    n += dn
