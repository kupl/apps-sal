import numpy as np

N = int(input())

S = list(map(int, input().split()))
T = list(map(int, input().split()))
U = np.array(list(map(int, input().split())), dtype=np.uint64)
V = np.array(list(map(int, input().split())), dtype=np.uint64)

ans = np.zeros((N, N), dtype=np.uint64)

for n in range(64):
    u = (U >> n) & 1
    v = (V >> n) & 1
    su = [int(S[i] * 2 + u[i]) for i in range(N)]
    tv = [int(T[i] * 2 + v[i]) for i in range(N)]
    suzerozero = []
    suoneone = []
    tvzerozero = []
    tvoneone = []
    for i in range(N):
        if su[i] == 0:
            suzerozero.append(i)
        if su[i] == 3:
            suoneone.append(i)
    for i in range(N):
        if tv[i] == 0:
            tvzerozero.append(i)
        if tv[i] == 3:
            tvoneone.append(i)

    b = np.zeros((N, N), dtype=np.uint64)
    ###行のAND=1とOR=0を埋める###
    for i in range(N):
        if su[i] == 1:
            b[i] = np.ones(N, int)
    ###列のAND=1とOR=0を埋める###
    for i in range(N):
        if tv[i] == 1:
            b[:, i] = np.ones(N, int)
    ###行と列の値が一致するところを埋める###
    b |= np.dot(np.array([u]).T, np.ones((1, N), dtype=np.uint64)) & np.dot(np.array([v]).T, np.ones((1, N), dtype=np.uint64)).T
    ###行のOR=1を満たしていく###
    if 1 not in tv and 3 not in tv:
        m = len(tvzerozero)
        now = 0
        for i in suoneone:
            b[i][tvzerozero[now % m]] += 1
            now += 1
    ###列のOR=1を満たしていく###
    if 1 not in su and 3 not in su:
        m = len(suzerozero)
        now = 0
        for i in tvoneone:
            b[suzerozero[now % m]][i] += 1
            now += 1
    ans += b << n


def end():
    print((-1))
    return


for i in range(N):
    if S[i] == 0:
        now = ans[i][0]
        for j in range(1, N):
            now &= ans[i][j]
    if S[i] == 1:
        now = ans[i][0]
        for j in range(1, N):
            now |= ans[i][j]
    if now != U[i]:
        end()
for i in range(N):
    if T[i] == 0:
        now = ans[0][i]
        for j in range(1, N):
            now &= ans[j][i]
    if T[i] == 1:
        now = ans[0][i]
        for j in range(1, N):
            now |= ans[j][i]
    if now != V[i]:
        end()

for item in ans:
    print((*list(item)))
