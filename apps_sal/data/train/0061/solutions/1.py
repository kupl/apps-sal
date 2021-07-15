for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    temp=0
    for i in range(1,N-1):
        if(A[i]>A[i-1] and A[i]>A[i+1]):
            temp=1
            print("YES")
            print(i,i+1,i+2)
            break
    if(temp==0):
        print("NO")
