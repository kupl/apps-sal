N = int(input())


def solve(N):
    cnt = 0
    cnt += N // 11 * 2
    N %= 11
    if 0 < N <= 6:
        cnt += 1
    elif 6 < N < 11:
        cnt += 2
    return cnt


print(solve(N))
