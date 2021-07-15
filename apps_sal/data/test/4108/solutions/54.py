import sys


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


S = IN_S()
T = IN_S()

d1 = dict()
d2 = dict()

len_s = len(S)

for i in range(len_s):
    a = S[i]
    b = T[i]
    if (a in d1 and d1[a] != b) or (b in d2 and d2[b] != a):
        print('No')
        return
    d1[a] = b
    d2[b] = a

print('Yes')

