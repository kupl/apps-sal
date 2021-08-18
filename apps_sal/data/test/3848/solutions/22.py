import sys
from math import log2, floor, ceil, sqrt, gcd
import bisect


def Ri(): return [int(x) for x in sys.stdin.readline().split()]
def ri(): return sys.stdin.readline().strip()


def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
def Yes(): print('Yes')
def No(): print('No')
def YES(): print('YES')
def NO(): print('NO')


INF = 10 ** 18
MOD = 1000000007

n, k = Ri()
st = ri()
st = [i for i in st]
arr = [chr(ord('a') + i) for i in range(k)]
flag = -1
ch = -1
if n == 1:
    if st[0] == arr[-1]:
        NO()
    else:
        print(chr(ord(st[0]) + 1))
else:
    for i in range(n - 1, -1, -1):
        for j in range(ord(st[i]) - ord('a') + 1, k):
            tch = arr[j]
            if i - 2 >= 0:
                if tch == st[i - 1] or tch == st[i - 2]:
                    continue
                else:
                    flag = i
                    ch = tch
                    break
            elif i - 1 >= 0:
                if tch == st[i - 1]:
                    continue
                else:
                    flag = i
                    ch = tch
                    break
            else:
                flag = i
                ch = tch
                break
        if flag != -1:
            break
    if flag == -1:
        NO()
    else:
        st[flag] = ch
        for i in range(flag + 1, n):
            for j in range(0, k):
                tch = arr[j]
                if i - 2 >= 0:
                    if tch == st[i - 1] or tch == st[i - 2]:
                        continue
                    else:
                        flag = i
                        ch = tch
                        st[i] = ch
                        break
                elif i - 1 >= 0:
                    if tch == st[i - 1]:
                        continue
                    else:
                        flag = i
                        ch = tch
                        st[i] = ch
                        break
                else:
                    flag = i
                    ch = tch
                    st[i] = ch
                    break
        print("".join(st))
