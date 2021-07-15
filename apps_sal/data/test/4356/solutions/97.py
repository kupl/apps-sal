N, M = list(map(int, input().split()))
A = []
B = []
clear = 0
same = 0
for i in range(N):
    A.append(str(input()))
for i in range(M):
    B.append(str(input()))

for i in range(N - M + 1):
    for j in range(N - M + 1):
        same = 0
        for k in range(M):
            if A[i + k][j: j + M] == B[k]:
                same += 1
            else:
                break
        if same == M:
            clear = 1
            break

if clear == 1:
    print('Yes')
else:
    print('No')

        

