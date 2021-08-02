import sys
N = int(input())
a = [int(input()) for _ in range(N)]
flag = [0] * N
k = 0
i = 0
flag[0] = 1
while k < N:
    k += 1
    i = a[i] - 1
    if flag[i] == 0:
        flag[i] = 1
    elif flag[i] == 1:
        print(-1)
        return
    if i == 1:
        print(k)
        return
