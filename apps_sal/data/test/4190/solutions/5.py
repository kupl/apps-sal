import sys
import bisect
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ALLB = [0] * n
LIST = []
for b in B:
    ALLB[b] += 1
    LIST.append(b)
LIST = sorted(set(LIST))
R = [0] * n
L = [0] * n
for i in range(len(LIST) - 1):
    R[LIST[i]] = LIST[i + 1]
for i in range(1, len(LIST)):
    L[LIST[i]] = LIST[i - 1]
R[LIST[len(LIST) - 1]] = LIST[0]
L[LIST[0]] = LIST[-1]
ANS = []
for a in A:
    x = bisect.bisect_left(LIST, -a % n)
    if x == len(LIST):
        x = 0
    y = LIST[x]
    if ALLB[y] > 0:
        ANS.append((a + y) % n)
        ALLB[y] -= 1
        if ALLB[y] == 0:
            (L[R[y]], R[L[y]]) = (L[y], R[y])
    else:
        ZLIST = []
        z = R[y]
        while ALLB[z] == 0:
            ZLIST.append(z)
            z = R[z]
        for k in ZLIST:
            R[k] = z
            L[k] = L[z]
        ANS.append((a + z) % n)
        ALLB[z] -= 1
        if ALLB[z] == 0:
            (L[R[z]], R[L[z]]) = (L[z], R[z])
print(*ANS)
