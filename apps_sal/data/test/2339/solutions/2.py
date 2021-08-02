def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


for i in ' ' * (int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    M = [0]
    MM = []
    check = [False] * n
    for i in range(n):
        ct = 0
        pt = -1
        for j in range(n):
            if not check[j]:
                k = gcd(M[-1], L[j])
                if k > ct:
                    ct = k
                    pt = j
        M.append(ct)
        MM.append(pt)
        check[pt] = True
    for j in MM: print(L[j], end=' ')
    print()
