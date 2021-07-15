t=int(input())
while t:
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    print(min(sum(a),m))
    t-=1
