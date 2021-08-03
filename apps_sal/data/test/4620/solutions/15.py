N = int(input())
CSF = [list(map(int, input().split(" "))) for _ in range(N - 1)]

for i in range(N):
    Time = 0
    for j in range(i, N - 1):
        c, s, f = CSF[j]
        Time = max(Time, s)
        if Time % f != 0:
            Time += (f - Time % f)
        Time += c

    print(Time)
