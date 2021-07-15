N = int(input())
ANS = [2, 1]
for i in range(1, N):
    ANS.append(ANS[i]+ANS[i-1])
print(ANS[N])
