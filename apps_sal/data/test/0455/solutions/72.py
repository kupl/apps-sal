import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
X, Y = [], []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
mod = (X[0] + Y[0]) % 2
for i in range(1, n):
    if (X[i] + Y[i]) % 2 != mod:
        print(-1)
        return
if not mod:
    X = [x + 1 for x in X]
U = [X[i] + Y[i] for i in range(n)]
V = [X[i] - Y[i] for i in range(n)]
Mode = ['L', 'D', 'U', 'R']
m = 31
if mod:
    print(m)
    print(' '.join([str(2**i) for i in range(m)]))
else:
    print(m + 1)
    print('1 ' + ' '.join([str(2**i) for i in range(m)]))
for i in range(n):
    w = ''
    if not mod:
        w = 'L'
    ui = (U[i] + 2**m - 1) // 2
    vi = (V[i] + 2**m - 1) // 2
    for _ in range(m):
        u_bit, v_bit = ui & 1, vi & 1
        ui >>= 1
        vi >>= 1
        w += Mode[u_bit * 2 + v_bit]
    print(w)
