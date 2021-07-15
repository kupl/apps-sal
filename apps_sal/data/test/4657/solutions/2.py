import sys
input = sys.stdin.readline

q=int(input())

for testcases in range(q):
    n,k=list(map(int,input().split()))
    A=list(map(int,input().split()))

    if sum(A)%2!=k%2:
        print("NO")
        continue

    ANS=[]
    SUM=0
    for i in range(n):
        SUM+=A[i]
        if SUM%2==1:
            ANS.append(i+1)
            SUM=0

    if len(ANS)>=k-1:
        print("YES")
        ANS0=ANS[:k-1]+[n]
        print(*ANS0)

    else:
        print("NO")

        
        

