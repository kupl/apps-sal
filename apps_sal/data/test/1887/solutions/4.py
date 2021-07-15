from collections import defaultdict
n = int(input())


a = list(map(int,input().split()))
b = list(map(int,input().split()))

score = [[0 for x in range(n)]for _ in range(2)]


if n == 1:
    print (max(a[0],b[0]))
    return
elif n==2:
    print (max(a[0]+b[1],b[0]+a[1]))
    return


score[0][0] = a[0]
score[1][0] = b[0]
score[1][1] = a[0]+b[1]
score[0][1] = b[0]+a[1]


for x in range(2,n):
    # where it has been used
    score[0][x] = max(score[1][x-1],score[1][x-2]) + a[x]
    score[1][x] = max(score[0][x-1],score[0][x-2])+ b[x]
print (max(score[0][-1],score[1][-1]))
