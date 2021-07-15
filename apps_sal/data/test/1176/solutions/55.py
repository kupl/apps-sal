N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(N):
    if A[i] < 0:
        cnt += 1
        A[i] *= -1
A.sort()
if cnt % 2 == 1:
    print(sum(A[1:])-A[0])
else:
    print(sum(A))
