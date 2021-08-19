n = int(input())
L = list(map(int, input().split()))
P = [-1 for _ in range(2000001)]


def premier(n):
    if P[n] >= 0:
        return P[n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            P[n] = False
            return False
    P[n] = True
    return True


e = L.count(1)
if n == 1:
    print(1)
    print(L[0])
elif e > 1:
    L.sort()
    i = 1
    while i < n and L[i] == 1:
        i += 1
    u = i
    ok = 0
    while i < n:
        if premier(L[i] + 1):
            print(u + 1)
            for j in range(u):
                print(1, end=' ')
            print(L[i])
            ok = 1
            break
        i += 1
    if ok == 0:
        print(u)
        for i in range(u):
            print(1, end=' ')
else:
    ok = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            t = premier(L[i] + L[j])
            if t:
                print(2)
                print(str(L[i]) + ' ' + str(L[j]))
                ok = 1
                break
        if ok:
            break
    if ok == 0:
        print(1)
        print(L[0])
