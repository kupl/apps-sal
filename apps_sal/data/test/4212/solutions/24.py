def backtrack(nums, N, cur_state, result):
    if len(cur_state) == N:
        result.append(cur_state[:])
    else:
        for i in range(len(nums)):
            cur_state.append(nums[i])
            backtrack(nums[i:], N, cur_state, result)
            cur_state.pop()


def solve():
    (N, M, Q) = [int(i) for i in input().split()]
    quads = []
    for i in range(Q):
        quads.append([int(i) for i in input().split()])
    candidates = []
    backtrack(list(range(1, M + 1)), N, [], candidates)
    ans = 0
    for candidate in candidates:
        score = 0
        for (a, b, c, d) in quads:
            if candidate[b - 1] - candidate[a - 1] == c:
                score += d
        ans = max(score, ans)
    print(ans)


def __starting_point():
    solve()


__starting_point()
