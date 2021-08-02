def sieve(n):
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1


n = int(input())
prime = [True for i in range(n + 2)]
prime[0] = 0
prime[1] = 0
sieve(n + 1)
aa = [0] * (n + 1)
for i in range(n + 1):
    if prime[i]:
        aa[i] = i
    else:
        aa[i] = aa[i - 1]
lis = [0] + list(map(int, input().split()))
ind = [0] * (n + 1)
ct = 0
for i in range(1, n + 1):
    ind[lis[i]] = i
ans = []
for i in range(1, n + 1):
    j = ind[i]
    while j > i:
        t = i
        step = aa[j - t + 1] - 1
        ct += 1
        ind[lis[j - step]] = j
        ind[lis[j]] = j - step
        ans.append([j - step, j])
        lis[j - step], lis[j] = lis[j], lis[j - step]
        j -= step
print(ct)
for i in ans:
    print(*i)
