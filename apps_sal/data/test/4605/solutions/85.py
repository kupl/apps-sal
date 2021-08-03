def solve(N, A, B):
    nums = []
    for n in range(1, N + 1):
        s = 0
        ns = str(n)
        for j in range(len(ns)):
            s += int(ns[j])
        if A <= s and s <= B:
            nums.append(n)
    print((sum(nums)))


def __starting_point():
    N, A, B = list(map(int, input().split()))
    solve(N, A, B)


__starting_point()
