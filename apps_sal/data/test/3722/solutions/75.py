#from collections import deque,defaultdict
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


n = inn()
aa = ins()
ab = ins()
ba = ins()
bb = ins()
if ab == 'A' and aa == 'A' or ab == 'B' and bb == 'B':
    print(1)
elif ab == 'A' and aa == 'B' and ba == 'A' or \
        ab == 'B' and bb == 'A' and ba == 'B':
    d = [0] * (n + 1)
    d[0] = 1
    for i in range(2, n + 1):
        for j in range(i - 1):
            d[i] = (d[i] + d[j]) % R
    print(d[n])
else:
    d = [0] * (n + 1)
    d[0] = 1
    x = 1
    for i in range(2, n - 1):
        for j in range(i - 1):
            d[i] = (d[i] + d[j] * (i - j - 1)) % R
        #ddprint(f"{i=} {x=} {d[i]=}")
        x = (x + d[i]) % R
    print(x)
