from collections import defaultdict


def solve(A, N):
    assert len(A) == N
    bitCover = defaultdict(int)
    for x in A:
        for i in range(32):
            if (1 << i) & x:
                bitCover[i] += 1
    # Everything that is covered will be deleted in the final result
    best = (0,)
    for j, x in enumerate(A):
        result = 0
        for i in range(32):
            if (1 << i) & x:
                if bitCover[i] == 1:
                    result += 1 << i
        best = max(best, (result, j))

    j = best[1]
    A = [A[j]] + A[:j] + A[j + 1 :]
    return ' '.join(map(str, A))


def __starting_point():
    N, = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(A, N)
    print(ans)

__starting_point()
