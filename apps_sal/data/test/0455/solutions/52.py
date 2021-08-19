import numpy as np
N = int(input())
XY = np.array([[int(x) for x in input().split()] for _ in range(N)], dtype=np.int64)
X = XY[:, 0]
Y = XY[:, 1]
command = np.array([''] * N, dtype=object)


def solve(k, X, Y, arms, command):
    if k == -1:
        return solve_final(X, Y, arms, command)
    bl_X = np.abs(X) > np.abs(Y)
    bl_Y = ~bl_X
    negative_X = X < 0
    negative_Y = Y < 0
    L = bl_X & negative_X
    R = bl_X & ~negative_X
    D = bl_Y & negative_Y
    U = bl_Y & ~negative_Y
    command[L] += 'L'
    command[R] += 'R'
    command[D] += 'D'
    command[U] += 'U'
    p = 1 << k
    arms.append(p)
    X[L] += p
    X[R] -= p
    Y[D] += p
    Y[U] -= p
    return solve(k - 1, X, Y, arms, command)


def solve_final(X, Y, arms, command):
    s = np.abs(X) + np.abs(Y)
    bl0 = (s == 0).all()
    bl1 = (s == 1).all()
    if bl0:
        return (arms, command)
    elif not bl1:
        return (None, None)
    arms.append(1)
    L = X == -1
    R = X == 1
    D = Y == -1
    U = Y == 1
    command[L] += 'L'
    command[R] += 'R'
    command[D] += 'D'
    command[U] += 'U'
    return (arms, command)


(arms, command) = solve(35, X, Y, [], command)
if arms is None:
    print(-1)
else:
    print(len(arms))
    print(' '.join([str(x) for x in arms]))
    print('\n'.join(command))
