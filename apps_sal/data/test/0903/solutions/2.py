import sys
input = sys.stdin.readline

n,k=list(map(int,input().split()))
A=sorted(map(int,input().split()),reverse=True)

MIN=1
MAX=max(A)+k


while MIN!=MAX:
    AVE=(MIN+MAX+1)//2

    score=0

    for i in range(n//2+1):
        if AVE>A[i]:
            score+=AVE-A[i]

    if score>k:
        MAX=AVE-1
    else:
        MIN=AVE

print(MIN)
        
        
    

