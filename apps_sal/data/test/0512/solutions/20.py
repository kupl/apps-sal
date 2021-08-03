def check():
    N = int(input())
    up, down = [0] * (2 * N + 1), [0] * (2 * N + 1)
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for a, b in zip(A, B):
        if 0 < b <= a or b == 1 or a == 2 * N:
            return 'No'
        if a == -1:
            pass
        elif up[a] == 0:
            up[a] = b
        else:
            return 'No'
        if b == -1:
            pass
        elif down[b] == 0:
            down[b] = a
        else:
            return 'No'
    dp = [[(i - j) % 2 for j in range(2 * N + 1)] for i in range(2 * N)]
    for l in range(1, 2 * N):
        if l % 2 == 1:
            x = (l + 1) // 2
            for left in range(1, 2 * N - l + 1):
                for y in range(left, left + x):
                    if (up[y] > 0 and up[y] != y + x) or down[y] != 0:
                        dp[left][left + l] = 0
                    if up[y + x] != 0 or (down[y + x] > 0 and down[y + x] != y):
                        dp[left][left + l] = 0
                    if up[y] == -1 and down[y + x] == -1:
                        dp[left][left + l] = 0
            if l == 1:
                continue
        for left in range(1, 2 * N + 1 - l):
            right = left + l
            for a in range(left + 1, right - 1):
                dp[left][right] |= dp[left][a] & dp[a + 1][right]
    if dp[1][-1] == 1:
        return 'Yes'
    return 'No'


print(check())
