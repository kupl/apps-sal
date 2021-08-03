def main():
    M = [0] * 4
    for i in range(4):
        M[i] = list(map(int, input().split()))

    W = [[0] * 2 for i in range(2)]
    for i in range(0, 2):
        for j in range(2, 4):
            if M[i][0] > M[j][1] and M[i ^ 1][1] > M[j ^ 1][0]:
                W[i][j - 2] = 1
            elif M[i][0] < M[j][1] and M[i ^ 1][1] < M[j ^ 1][0]:
                W[i][j - 2] = -1
            else:
                W[i][j - 2] = 0
    if max(W[0][0] + W[0][1], W[1][0] + W[1][1]) == 2:
        print("Team 1")
    elif min(W[0][0], W[0][1]) + min(W[1][0], W[1][1]) == -2:
        print("Team 2")
    else:
        print("Draw")


main()
