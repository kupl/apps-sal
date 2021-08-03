import math

N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N):
    t = 0

    for c, s, f in CSF[i:]:
        # 待ち時間
        if t < s:
            t = s
        else:
            t = math.ceil((t - s) / f) * f + s

        # i -> i+1に移動
        t += c

    print(t)
