# Some people dream of success, while others wake up and work hard at it. Napoleon Hill
# by : Blue Edge - Create some chaos

for _ in range(int(input())):
    l,r=list(map(int,input().split()))
    if r<2*l:
        print(-1,-1)
    else:
        print(l,2*l)

