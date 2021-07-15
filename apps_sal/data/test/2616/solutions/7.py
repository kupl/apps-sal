import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ones=0
    for i in arr:
        if i==1:
            ones+=1
        else:
            break
    if(ones<n):
        if(ones%2==0):
            print("First")
        else:
            print("Second")
    else:
        if(ones%2==1):
            print("First")
        else:
            print("Second")

        

