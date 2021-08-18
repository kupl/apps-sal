import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]
def dp3(ini, i, j, k): return [[[ini] * i for _ in range(j)] for _ in range(k)]


H, W = mi()
N = ii()
A = li()

table = dp2(0, W, H)
i = -1
j = 0
for ind in range(N):
    a = A[ind]
    while a > 0:
        if i + 1 < H and not table[i + 1][j]:
            table[i + 1][j] = ind + 1
            i += 1
        elif j + 1 < W and not table[i][j + 1]:
            table[i][j + 1] = ind + 1
            j += 1
        else:
            if i > 0 and not table[i - 1][j]:
                table[i - 1][j] = ind + 1
                i -= 1
            elif j > 0 and not table[i][j - 1]:
                table[i][j - 1] = ind + 1
                j -= 1
        a -= 1

for i in range(H):
    for j in range(W):
        print(table[i][j], '', end='')
    print('')
