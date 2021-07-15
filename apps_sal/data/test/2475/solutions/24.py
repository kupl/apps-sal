import sys
input = sys.stdin.readline

N=int(input())
S=list(map(int,input().split()))

ANS=0

for i in range(1,N//2):
    s=0
    l=N-1
    SCORE=0

    if (N-1)%i==0:
        while l>s and l>i:

            SCORE+=S[s]+S[l]
            ANS=max(ANS,SCORE)
            s+=i
            l-=i
        #print(SCORE,i,l,s)
    else:
        while l!=s and l>i:

            SCORE+=S[s]+S[l]
            ANS=max(ANS,SCORE)
            s+=i
            l-=i

        #print(SCORE,i,l,s)

print(ANS)
