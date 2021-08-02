N = int(input())
A = list(map(int, input().split()))
R = [0] * 9

for a in A:
    if a < 400:
        R[0] += 1
    elif a < 800:
        R[1] += 1
    elif a < 1200:
        R[2] += 1
    elif a < 1600:
        R[3] += 1
    elif a < 2000:
        R[4] += 1
    elif a < 2400:
        R[5] += 1
    elif a < 2800:
        R[6] += 1
    elif a < 3200:
        R[7] += 1
    else:
        R[8] += 1

if sum(R[:-1]) != 0:
    M = 8 - R[:-1].count(0) + R[-1]
    m = 8 - R[:-1].count(0)
    print(m, M)
else:
    print(1, R[-1])
