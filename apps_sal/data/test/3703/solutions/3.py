phi = [0 for i in range(100100)]
phi[1] = 1
for i in range(2, 100050):
    if (phi[i] == 0):
        for j in range(i, 100051, i):
            if (phi[j] == 0):
                phi[j] = j
            phi[j] = phi[j] // i * (i - 1)


def Fenjie(n):
    k = {}
    if (n == 1):
        return {}
    a = 2
    while (n >= 2):
        b = n % a
        if (a * a > n):
            if (n in k):
                k[n] += 1
            else:
                k[n] = 1
            break
        if (b == 0):
            if (a in k):
                k[a] += 1
            else:
                k[a] = 1
            n = n // a
        else:
            a += 1
    return k


def Euler(k):
    if (len(k) == 0):
        return 1
    ans = 1
    for i in k:
        s = k[i]
        ans *= pow(i, s)
        ans = ans // i * (i - 1)
    return ans


n, k = list(map(int, input().split()))
k = (k + 1) // 2
while (k):
    k -= 1
    n = Euler(Fenjie(n))
    if (n == 1):
        break
print(n % (10**9 + 7))
