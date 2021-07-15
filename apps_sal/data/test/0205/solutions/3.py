from math import sqrt
def fact(a):
    nonlocal g
    nonlocal h
    for i in range(2, int(sqrt(a)) + 1):
        k = 0
        if a % i == 0:
            g.append(i)
        while a % i == 0:
            a = a // i
            k += 1
        if k != 0:
            h.append(k)
    if a > 1:
        g.append(a)
        h.append(1)
n, k = list(map(int, input().split()))
g = []
h = []
f = fact(k)
mini = 100000000000000000000000000000000000000000000000000000000000
for i in range(len(g)):
    k1 = 0
    v = g[i]
    while n // g[i] > 0:
        k1 += n // g[i]
        g[i] *= v
    if k1 // h[i] < mini:
        mini = k1 // h[i]
print(mini)

