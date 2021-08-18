def solve(S, K):
    ans = ''
    for i in range(len(S)):
        if i + 1 == K:
            ans = S[i]
            break
        if S[i] != '1':
            ans = S[i]
            break
    print(ans)


def __starting_point():
    S = input()
    K = int(input())
    solve(S, K)


__starting_point()
