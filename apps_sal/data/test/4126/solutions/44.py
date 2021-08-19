def main():
    S = input()
    N = len(S)
    for i in range(N):
        if S[i] != S[N - i - 1]:
            print('No')
            return
    M = (N - 1) // 2
    for i in range(M):
        if S[i] != S[N - i - 1]:
            print('No')
            return
    L = (N + 3) // 2 - 1
    for i in range(L, N):
        if S[i] != S[N + L - i - 1]:
            print('No')
            return
    print('Yes')


main()
