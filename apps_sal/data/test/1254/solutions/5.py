import sys
input = sys.stdin.readline

n,m=list(map(int,input().split()))
SR=[list(map(int,input().split())) for i in range(n)]

LIST=[[] for i in range(m+1)]

for s,r in SR:
    LIST[s].append(r)

LENLIST=[0]*(m+1)
for i in range(1,m+1):
    LIST[i].sort(reverse=True)
    LENLIST[i]=len(LIST[i])

LISTSUM=[[] for i in range(m+1)]

for i in range(1,m+1):
    if LIST[i]==[]:
        continue
    LISTSUM[i].append(LIST[i][0])

    for j in range(1,LENLIST[i]):
        LISTSUM[i].append(LISTSUM[i][-1]+LIST[i][j])

LEN=len(max(LIST,key=lambda x:len(x)))

ANS=[0]*LEN

for j in range(1,m+1):
    for i in range(LENLIST[j]):
        if LISTSUM[j][i]>0:
            ANS[i]+=LISTSUM[j][i]
        else:
            break

print(max(ANS))

