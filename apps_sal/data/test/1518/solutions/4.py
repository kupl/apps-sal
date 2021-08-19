def sieve(n):
    p = 2
    while (p * p <= n):
        if (prime[p] == False):
            for i in range(p * p, n + 1, p):
                prime[i] = True
        p += 1


n = int(input())
prime = [False for i in range(n + 2)]
prime[0] = 1
prime[1] = 1
sieve(n + 1)
lis = [0] + list(map(int, input().split()))
ind = [0] * (n + 1)
ct = 0
for i in range(1, n + 1):
    ind[lis[i]] = i
# print(prime,ind)
ans = []
for i in range(1, n + 1):
    j = ind[i]
    while j > i:
        t = i
        while prime[j - t + 1]:
            t += 1
#        print(j,t)
        ct += 1
        ind[lis[j]] = t
        ind[lis[t]] = j
        ans.append([t, j])
        lis[j], lis[t] = lis[t], lis[j]
        j = t
print(ct)
for i in ans:
    print(*i)
