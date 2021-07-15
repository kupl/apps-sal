#n = int(input())
n,m = list(map(int,input().split()))
val = n//m
if val%2==0:
    print("NO")
else:
    print("YES")

