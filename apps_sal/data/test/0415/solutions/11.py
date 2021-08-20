N = int(input())
A = list(map(int, input().split()))
SUM = [0]
for a in A:
    SUM.append(SUM[-1] + a)
ANS = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        if (SUM[j] - SUM[i]) / (j - i) > 100 and j - i > ANS:
            ANS = j - i
print(ANS)
