def f(gx,gy):
    ans = 10**9
    no = 0
    for i in range(m):
        tmp = abs(gx-checkpoint[i][0]) + abs(gy-checkpoint[i][1])
        if tmp < ans:
            ans = tmp
            no = i
    return no+1

n,m = list(map(int,input().split()))
gakusei = []
for i in range(n):
    x,y = list(map(int,input().split()))
    gakusei.append([x,y])
checkpoint = []
for j in range(m):
    x,y = list(map(int,input().split()))
    checkpoint.append([x,y])

#print(gakusei,checkpoint)
for i in range(n):
    print((f(gakusei[i][0],gakusei[i][1])))


