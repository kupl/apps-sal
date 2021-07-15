def resolve():
    S = list(input())
    if len(S) == 2:
        if S[0] == S[1]:
            print(1, 2)
        else:
            print(-1, -1)
        return
    for i in range(len(S)-2):
        if S[i] == S[i+1] or S[i+1] == S[i+2] or S[i+2] == S[i]:
            print(i+1, i+3)
            return
    print(-1, -1)


def __starting_point():
    resolve()
__starting_point()
