#from collections import deque,defaultdict
def printn(x): return print(x, end='')
def inn(): return int(input())
def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True  # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353


def ddprint(x):
    if DBG:
        print(x)


s = ins()
n = len(s)
ans = 0
for i in range(2**(n - 1)):
    z = []
    head = 0
    for j in range(n - 1):
        if (i >> j) % 2 > 0:
            z.append(int(s[head:j + 1]))
            head = j + 1
    z.append(int(s[head:]))
    ans += sum(z)
print(ans)
