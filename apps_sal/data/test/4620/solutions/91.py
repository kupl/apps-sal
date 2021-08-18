import math

N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N):
    t = 0

    for c, s, f in CSF[i:]:
        if t < s:
            t = s
        else:
            t = math.ceil((t - s) / f) * f + s

        t += c

    print(t)
