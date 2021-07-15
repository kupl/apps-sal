n,m = map(int,input().split())
xi = list(map(int,input().split()))
yi = list(map(int,input().split()))
ans = []
for i in xi:
    if i in yi:
        print(i,end=" ")

