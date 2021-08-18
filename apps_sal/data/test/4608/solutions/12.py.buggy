N = int(input())
A = [int(input()) for i in range(N)]
i = 0
cnt = 1
cmpr = [0]
while A[i] != 2:
    if A[i] == i + 1:
        print(-1)
        return
    i = A[i] - 1
    cmpr.append(i)
    cnt += 1
    if cnt > N:
        print(-1)
        return
print(cnt)
