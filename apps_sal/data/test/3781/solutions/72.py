from collections import defaultdict
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


t = inn()
for tt in range(t):
    n = inn()
    a = inl()
    if n % 2 > 0:
        print('Second')
    else:
        h = defaultdict(int)
        for x in a:
            h[x] += 1
        hasod = False
        for x in h:
            if h[x] % 2 > 0:
                hasod = True
                break
        print('First' if hasod else 'Second')
