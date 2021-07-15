from collections import Counter

N = int(input())
D = list(map(int,input().split()))

CD = Counter(D)
CD=list(CD.items())
count=0
for i in range(len(CD)):
    if CD[i][0]<CD[i][1]:
        count=count+CD[i][1]-CD[i][0]
    elif CD[i][0]>CD[i][1]:
        count=count+CD[i][1]
print(count)
