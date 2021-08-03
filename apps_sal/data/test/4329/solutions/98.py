import sys
stdin = sys.stdin


def ip(): return int(sp())
def fp(): return float(sp())
def lp(): return list(map(int, stdin.readline().split()))
def sp(): return stdin.readline().rstrip()


yp = 'Yes'
np = 'No'

s = sp()
t = sp()

l = len(s)

if s[0:l] == t[0:l]:
    print(yp)
else:
    print(np)
