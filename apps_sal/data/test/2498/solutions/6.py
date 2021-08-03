from math import gcd
def lcm(a, b): return (a * b) // (gcd(a, b))


def f(x):
    cnt = 0
    while(x % 2 == 0):
        cnt += 1
        x = x // 2
    return cnt


n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x // 2, a))

t = f(a[0])
for i in range(n):
    if(f(a[i]) != t):
        print(0)
        return
    a[i] = a[i] // (2**t)
m = m // (2**t)
l = 1
for i in range(n):
    l = lcm(l, a[i])
    if(l > m):
        print(0)
        return
m = m // l
print((m + 1) // 2)
