N = int(input())
C, S, F = [], [], []

for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for station in range(N):
    now = station
    time = 0

    while now < N-1:
        if time < S[now]:
            time = S[now] + C[now]
        else:
            if time % F[now] == 0:
                time += C[now]
            else:
                wait_time = F[now] - (time % F[now])
                time += wait_time + C[now]

        now += 1

    print(time)
