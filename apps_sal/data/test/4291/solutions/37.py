def solve(N, Q, S, LRi):
    cumulative_sum = [0, 0]
    for i in range(1, N):
        tmp = cumulative_sum[-1]
        if S[i - 1:i + 1] == 'AC':
            tmp += 1
        cumulative_sum.append(tmp)
    for (l, r) in LRi:
        print(cumulative_sum[r] - cumulative_sum[l])


def __starting_point():
    (N, Q) = list(map(int, input().split()))
    S = input()
    LRi = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, S, LRi)


__starting_point()
