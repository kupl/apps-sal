for _ in ' '*int(input()):
    a,b,c = map(int,input().split())
    print(max(abs(a-b)+abs(a-c)+abs(b-c)-4,0))
