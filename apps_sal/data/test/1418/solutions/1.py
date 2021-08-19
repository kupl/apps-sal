def SieveOfEratosthenes(n, ans):
    c = 1
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            ans[p] = c
            for i in range(p * p, n + 1, p):
                prime[i] = False
                ans[i] = c
            c += 1
        p += 1
    return c


n = int(input())
ans = [0] * (n + 1)
c = SieveOfEratosthenes(n, ans)
for i in range(2, n + 1):
    if ans[i] == 0:
        ans[i] = c
        c += 1
print(' '.join((str(x) for x in ans[2:])))
