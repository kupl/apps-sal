import numpy as np
N = int(input())
XY = np.array([[int(x) for x in input().split()] for _ in range(N)], dtype=np.int64)
X = XY[:, 0]
Y = XY[:, 1]
command = np.array([""] * N, dtype=object)


def solve(k, X, Y, arms, command):
    if k == -1:
        return final_solve(X, Y, arms, command)
    else:
        # 大きい方を変換
        # print(X,Y)
        bl_X = (np.abs(X) > np.abs(Y))
        bl_Y = ~bl_X
        neg_X = (X < 0)
        neg_Y = (Y < 0)
        L = bl_X & neg_X
        R = bl_X & (~neg_X)
        U = bl_Y & (~neg_Y)
        D = bl_Y & neg_Y
        p = 1 << k
        command[L] += "L"
        command[R] += "R"
        command[U] += "U"
        command[D] += "D"
        X[L] += p

        X[R] -= p

        Y[U] -= p

        Y[D] += p

        arms.append(p)
        return solve(k - 1, X, Y, arms, command)


def final_solve(X, Y, arms, command):
    s = np.abs(X) + np.abs(Y)
    b0 = (s == 0).all()
    b1 = (s == 1).all()
    if b0:
        return arms, command
    elif not b1:
        return None, None

    arms.append(1)
    L = (X == -1)
    R = (X == 1)
    D = (Y == -1)
    U = (Y == 1)
    command[L] += "L"
    command[R] += "R"
    command[U] += "U"
    command[D] += "D"
    return arms, command


arms, command = solve(35, X, Y, [], command)

if arms is None:
    print(-1)
else:
    print(len(arms))
    print(" ".join([str(i) for i in arms]))
    print("\n".join(command))
