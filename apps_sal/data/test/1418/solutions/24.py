n = int(input())
prime = [True for i in range(n + 1)]
l = [-1 for i in range(n + 1)]
p = 2
c = 0
while p * p <= n:
    if prime[p] == True:
        c += 1
        l[p] = c
        for i in range(p * p, n + 1, p):
            prime[i] = False
            l[i] = c
    p += 1
for i in range(2, n + 1):
    if l[i] == -1:
        c += 1
        print(c, end=' ')
    else:
        print(l[i], end=' ')
