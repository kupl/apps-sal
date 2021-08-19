T = int(input())
for t in range(T):
    N = int(input())
    M = []
    for i in range(N):
        M.append(input())
    inverts = []
    if M[0][1] == '0' and M[1][0] == '0':
        if M[N - 2][N - 1] == '0':
            inverts.append((N - 2, N - 1))
        if M[N - 1][N - 2] == '0':
            inverts.append((N - 1, N - 2))
    elif M[0][1] == '1' and M[1][0] == '1':
        if M[N - 2][N - 1] == '1':
            inverts.append((N - 2, N - 1))
        if M[N - 1][N - 2] == '1':
            inverts.append((N - 1, N - 2))
    elif M[0][1] == '0' and M[1][0] == '1':
        if M[N - 2][N - 1] == '1' and M[N - 1][N - 2] == '1':
            inverts.append((1, 0))
        if M[N - 2][N - 1] == '0' and M[N - 1][N - 2] == '0':
            inverts.append((0, 1))
        if M[N - 2][N - 1] == '1' and M[N - 1][N - 2] == '0':
            inverts.append((1, 0))
            inverts.append((N - 1, N - 2))
        if M[N - 2][N - 1] == '0' and M[N - 1][N - 2] == '1':
            inverts.append((1, 0))
            inverts.append((N - 2, N - 1))
    elif M[0][1] == '1' and M[1][0] == '0':
        if M[N - 2][N - 1] == '0' and M[N - 1][N - 2] == '0':
            inverts.append((1, 0))
        if M[N - 2][N - 1] == '1' and M[N - 1][N - 2] == '1':
            inverts.append((0, 1))
        if M[N - 2][N - 1] == '0' and M[N - 1][N - 2] == '1':
            inverts.append((1, 0))
            inverts.append((N - 1, N - 2))
        if M[N - 2][N - 1] == '1' and M[N - 1][N - 2] == '0':
            inverts.append((1, 0))
            inverts.append((N - 2, N - 1))
    print(len(inverts))
    for i in inverts:
        print(i[0] + 1, i[1] + 1)
