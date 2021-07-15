n,m = map(int,input().split())
lr = []
for i in range(m):
    LR = list(map(int,input().split()))
    lr.append(LR)
min,max = 1,n
for i in range(m):
    if lr[i][0] > min:
        min = lr[i][0]
    if lr[i][1] < max:
        max = lr[i][1]
if min > max:
    print("0")
else:
    print(max - min + 1)
