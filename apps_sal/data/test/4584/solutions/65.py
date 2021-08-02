N = int(input())
A = list(map(int, input().split()))

ANS = []
for i in range(N):
    ANS.append(0)


for i in range(N - 1):
    ANS[A[i] - 1] += 1

for i in range(N):
    print(ANS[i])
