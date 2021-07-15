N = int(input())
A = list([0]*N)
A = list(map(int, input().split()))

cnt = 0
flag = False
while 1:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = True
            break
        A[i] = A[i] /2
    if flag:
        break
    cnt += 1
print(cnt)
