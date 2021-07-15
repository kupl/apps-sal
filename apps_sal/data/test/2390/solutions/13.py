def main():
    N, C = list(map(int, input().split()))
    XV = [tuple(map(int, input().split())) for _ in range(N)]
    return max(solve(N, C, XV), solve(N, C, [(C - x, v) for x, v in reversed(XV)]))

def solve(N, C, XV):
    lv = [0] * N
    rv = [0] * N
    x0, c, m = 0, 0, 0
    for i, (x, v) in enumerate(XV):
        c += v - (x - x0)
        m = max(m, c)
        lv[i] = m
        x0 = x
    rv = [0] * N
    x0, c, m = C, 0, 0
    for i, (x, v) in enumerate(reversed(XV)):
        c += v - 2 * (x0 - x)
        m = max(m, c)
        rv[i] = m
        x0 = x
    for i in range(N - 1):
        lv[i] += rv[N - i - 2]
    return max(lv)

print((main()))

