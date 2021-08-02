a, b = map(int, input().split())
c = list(map(int, input().split()))
d, e = map(int, input().split())
f = list(map(int, input().split()))
n1 = 0
n2 = 0
for i in range(len(c)):
    n1 += c[i] * b**(len(c) - i - 1)
for i in range(len(f)):
    n2 += f[i] * e**(len(f) - i - 1)
if n1 > n2:
    print('>')
elif n1 == n2:
    print('=')
else:
    print('<')
