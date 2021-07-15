import sys
input = sys.stdin.readline

t=int(input())

for testcases in range(t):
    n=int(input())
    A=list(map(int,input().split()))

    LIST=[[] for i in range(n+1)]

    for ind,a in enumerate(A):
        LIST[a].append(ind)

    ANS=n+10

    for i in range(n+1):
        if len(LIST[i])<2:
            continue
        for j in range(1,len(LIST[i])):
            ANS=min(ANS,LIST[i][j]-LIST[i][j-1])

    if ANS==n+10:
        print(-1)
    else:
        print(ANS+1)

