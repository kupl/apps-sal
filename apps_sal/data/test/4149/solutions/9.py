import sys
input = sys.stdin.readline
n = int(input())
a = [int(x) for x in input().strip().split()]
dic = {}
for e in a:
    if e not in dic:
        dic[e] = 0
    dic[e] += 1


def primes_method5(n):
    out = list()
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return out


prime = primes_method5(2750132)
prime_set = set(prime)
arr_prime = []
res = []
for e in a:
    if e in prime_set:
        arr_prime.append(e)
    else:
        res.append(e)
ans = []
arr_prime.sort()
arr_primeset = set(arr_prime)
res.sort(reverse=True)
res_set = set(res)
for r in res:
    if dic[r] > 0:
        for p in prime:
            if r % p == 0:
                div = r // p
                if div in dic:
                    dic[div] -= 1
                    dic[r] -= 1
                    ans.append(r)
                else:
                    pass
                break
for x in arr_prime:
    if dic[x] > 0:
        if prime[x - 1] in arr_primeset and dic[prime[x - 1]] > 0:
            ans.append(x)
            dic[x] -= 1
            dic[prime[x - 1]] -= 1
print(*ans)
