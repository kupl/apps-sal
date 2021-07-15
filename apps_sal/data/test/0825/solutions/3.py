import collections

#https://note.nkmk.me/python-prime-factorization/
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def f(n):
    for i in range(1,20):
        if n<(i*(i+1))//2:
            return i-1

n = int(input())
c = collections.Counter(prime_factorize(n))
ans = 0
for i in c.keys():
    ans += f(c[i])
print(ans)
