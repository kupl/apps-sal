N = int(input())
H = list(map(int, input().split()))
cnt = 0
CNT = []
ANS = []
for i in range(1, N):
    if H[i] <= H[i - 1]:
        CNT.append(1)
    else:
        CNT.append(0)
for i in range(N - 1):
    if CNT[i] == 0:
        ANS.append(cnt)
        cnt = 0
    elif CNT[i] == 1:
        cnt += 1
ANS.append(cnt)
print(max(ANS))
