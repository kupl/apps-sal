from sys import stdin,stdout
n=int(stdin.readline().strip())
for i in range(n):
    n,m=list(map(int,stdin.readline().strip().split()))
    if(n-m==1):
        print("NO")
    else:
        print("YES")

