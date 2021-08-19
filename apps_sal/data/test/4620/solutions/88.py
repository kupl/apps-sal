N = int(input())
csf = []
for _ in range(N - 1):
    csf.append(list(map(int, input().split())))
for i in range(N):
    if i < N - 1:
        t = csf[i][1]
        for i in range(i, N - 1):
            (c, s, f) = csf[i]
            if t >= s:
                if t % f == 0:
                    t += c
                else:
                    t = -(-t // f) * f + c
            else:
                t = s + c
        print(t)
    else:
        print(0)
