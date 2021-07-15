import sys
input = sys.stdin.readline

a,b,c,d=list(map(int,input().split()))

for start in range(4):
    ANS=[]
    now=start
    A=[a,b,c,d]

    if A[now]==0:
        continue

    while True:
        A[now]-=1
        ANS.append(now)

        if now==0:
            if A[1]!=0:
                now=1
            else:
                break

        elif now==1:
            if A[0]!=0:
                now=0
            elif A[2]!=0:
                now=2
            else:
                break

        elif now==2:
            if A[3]!=0:
                now=3
            elif A[1]!=0:
                now=1
            else:
                break
        else:
            if A[2]!=0:
                now=2
            else:
                break

    if max(A)==0:
        print("YES")
        print(*ANS)
        return
print("NO")
        

