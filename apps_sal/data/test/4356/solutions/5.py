import math
N, M = list(map(int, input().split()))
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for i in range(0, math.ceil(N / M)):
    for j in range(0, math.ceil(N / M)):
        # 畳み込み
        flag = True
        for l in range(0, M):
            for m in range(0, M):
                if A[l + i][m + j] != B[l][m]:
                    flag = False
                    break
        if flag == True:
            print("Yes")
            return
print("No")
