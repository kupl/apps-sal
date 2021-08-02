from collections import defaultdict
printn = lambda x: print(x, end='')
inn = lambda: int(input())
inl = lambda: list(map(int, input().split()))
inm = lambda: map(int, input().split())
ins = lambda: input().strip()
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
