import sys
input = sys.stdin.readline


def rr(n):
    a = set([])
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            a.add(p)
    return a


def pal(a):
    if str(a) == str(a)[::-1]:
        return 1
    return 0


(p, q) = list(map(int, input().split()))
n = 1500000
a = rr(n)
b = []
c = 0
d = 0
for i in range(1, n + 1):
    if i in a:
        c += 1
    d += pal(i)
    b.append([c / d, i])
e = -1
for i in range(len(b) - 1, -1, -1):
    if b[i][0] <= p / q:
        e = b[i][1]
        break
if e == -1:
    print('Palindromic tree is better than splay tree')
else:
    print(e)
