def rev(a, m):
    res = 1
    k = m-2
    s = a
    while k > 0:
        if k%2 == 1:
            res = (res * s) % m
        k //= 2
        s = (s**2) % m
    return res

n, m = [int(x) for x in input().split()]
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
a = []
mul = 1
for x,y in zip(a1, a2):
    if x == 0 and y == 0:
        count = (m*(m-1))//2
        counteq = m
        maxcount = m**2
    elif x == 0:
        count = m - y
        counteq = 1
        maxcount = m
    elif y == 0:
        count = x-1
        counteq = 1
        maxcount = m
    else:
        count = 1 if x>y else 0
        counteq = 1 if x==y else 0
        maxcount = 1

    a.append((count, counteq, maxcount))
    if counteq == 0: break
a.reverse()

##print(a)

P, Q = 0, 1
for c, ce, mc in a:
    P = (P*ce+ Q*c) % (10**9+7)
    Q = (Q*mc)  % (10**9+7)
  

res, zeros = P, Q
print((res * rev(zeros, 10**9+7)) % (10**9+7))

