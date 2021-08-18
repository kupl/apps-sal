N = int(input())
S = input()
S = [1 if S[i] == 'o' else -1 for i in range(N)]

# 0番目は羊のパターン
tmp = [0] * N
tmp[0] = 1
if S[0] == 1:  # 0番目の両隣は同種
    # 0番目の両隣は羊
    tmp[1] = 1
    tmp[N - 1] = 1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

    # 0番目の両隣は狼
    tmp[1] = -1
    tmp[N - 1] = -1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

else:  # 0番目の両隣は異種
    # 1番目が羊, N-1番目が狼
    tmp[1] = 1
    tmp[N - 1] = -1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

    # 1番目が狼, N-1番目が羊
    tmp[1] = -1
    tmp[N - 1] = 1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

# 0番目は狼のパターン
tmp = [0] * N
tmp[0] = -1
if S[0] == -1:  # 0番目の両隣は同種
    # 0番目の両隣は羊
    tmp[1] = 1
    tmp[N - 1] = 1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

    # 0番目の両隣は狼
    tmp[1] = -1
    tmp[N - 1] = -1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

else:  # 0番目の両隣は異種
    # 1番目が羊, N-1番目が狼
    tmp[1] = 1
    tmp[N - 1] = -1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

    # 1番目が狼, N-1番目が羊
    tmp[1] = -1
    tmp[N - 1] = 1

    for i in range(2, N - 1):
        tmp[i] = tmp[i - 1] * tmp[i - 2] * S[i - 1]

    if tmp[N - 1] == tmp[N - 2] * tmp[N - 3] * S[N - 2] and tmp[0] == tmp[N - 1] * tmp[N - 2] * S[N - 1]:
        ans = ['S' if tmp[i] == 1 else 'W' for i in range(N)]
        print(''.join(ans))
        return

print(-1)
