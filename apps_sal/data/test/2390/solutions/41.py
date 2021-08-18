

N, C = list(map(int, input().split()))

xv = [tuple(map(int, input().split())) for _ in range(N)]


accum_clockwise = [None] * N
accum_clockwise[0] = xv[0]
tmp = xv[0][1]
for i in range(1, N):
    tmp += xv[i][1]
    accum_clockwise[i] = (xv[i][0], tmp)

accum_anticlockwise = [None] * N
accum_anticlockwise[0] = (C - xv[-1][0], xv[-1][1])
tmp = xv[-1][1]
for i in range(1, N):
    tmp += xv[N - 1 - i][1]
    accum_anticlockwise[i] = (C - xv[N - 1 - i][0], tmp)


max_clockwise = [0] * (N + 1)
for i in range(N):
    max_clockwise[i + 1] = max(max_clockwise[i], accum_clockwise[i][1] - accum_clockwise[i][0] * 2)


max_anticlockwise = [0] * (N + 1)
for i in range(N):
    max_anticlockwise[i + 1] = max(max_anticlockwise[i], accum_anticlockwise[i][1] - accum_anticlockwise[i][0] * 2)


ans_clockwise = 0
for i in range(N):
    ans_clockwise = max(ans_clockwise, accum_clockwise[i][1] - accum_clockwise[i][0] + max_anticlockwise[N - 1 - i])

ans_anticlockwise = 0
for i in range(N):
    ans_anticlockwise = max(ans_anticlockwise, accum_anticlockwise[i][1] - accum_anticlockwise[i][0] + max_clockwise[N - 1 - i])

print((max(ans_clockwise, ans_anticlockwise)))
