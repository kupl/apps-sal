N=int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]
three=[]
for i in range(N):
    if x[i]==y[i]:
        three.append(1)
    else:
        three.append(0)

cnt=0
max=0
for i in range(N-1):
    if three[i]==1 and three[i+1]==1:
        cnt+=1
        if max<cnt:
            max=cnt
    else:
        cnt=0

if max+1>=3:
    print('Yes')
else:
    print('No')
