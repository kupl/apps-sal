from numba import njit, i8


@njit(i8(i8))
def solve(N):
    ans = 0
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            ans += j
    return ans


N = int(input())
print(solve(N))
