s = input()
ast = s.split(' ')
n, k = int(ast[0]), int(ast[1])
s = input()
a = [int(i) for i in s.split(' ')]
s = input()
b = [int(i) for i in s.split(' ')]
L = n // k
p = 10**k
r = 10**(k - 1)
rez = 1
for i in range(L):
    cnt = 0
    if b[i] > 0:
        cnt += (b[i] * r - 1) // a[i]
        cnt += (p - 1) // a[i]
        cnt -= ((b[i] + 1) * r - 1) // a[i]
        rez *= cnt + 1
    else:
        cnt += (p - 1) // a[i]
        cnt -= (r - 1) // a[i]
        rez *= cnt
    rez = rez % (10**9 + 7)
print(rez)
