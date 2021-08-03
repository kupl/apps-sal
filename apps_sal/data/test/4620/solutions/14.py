N = int(input())
CSF = [[] for T in range(0, N - 1)]
for TN in range(0, N - 1):
    CSF[TN] = [int(T) for T in input().split()]
for TN in range(0, N):
    Time = 0
    for TT in range(TN, N - 1):
        if Time >= CSF[TT][1]:
            Time += CSF[TT][0] + (CSF[TT][2] - (Time % CSF[TT][2])) % CSF[TT][2]
        else:
            Time += CSF[TT][0] + (CSF[TT][1] - Time)
    print(Time)
