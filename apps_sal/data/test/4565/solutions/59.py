def solve(N, S):
    W_sum = [0]
    E_sum = [0]
    for s in list(S):
        if s == 'W':
            W_sum.append(W_sum[-1] + 1)
            E_sum.append(E_sum[-1])
        else:
            W_sum.append(W_sum[-1])
            E_sum.append(E_sum[-1] + 1)
    ans = N + 1
    for i in range(1, N + 1):
        ans = min(W_sum[i - 1] + (E_sum[-1] - E_sum[i]), ans)
    print(ans)


def __starting_point():
    N = int(input())
    S = input()
    solve(N, S)


__starting_point()
