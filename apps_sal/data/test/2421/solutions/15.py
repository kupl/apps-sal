import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    lis = list(map(int,input().split()))
    costs = [0]*6
    costs[0] = min(lis[0],lis[1]+lis[5])
    costs[1] = min(lis[1],lis[0]+lis[2])
    costs[2] = min(lis[2],lis[1]+lis[3])
    costs[3] = min(lis[3],lis[2]+lis[4])
    costs[4] = min(lis[4],lis[3]+lis[5])
    costs[5] = min(lis[5],lis[4]+lis[0])
    ans = 0
    if x >= 0 and y >= 0:
        ans += min(x,y) * costs[0]
        if x >= y:
            ans += (x-y) * costs[5]
        else:
            ans += (y-x) * costs[1]
    elif x <= 0 and y <= 0:
        ans += min(abs(x),abs(y)) * costs[3]
        if x <= y:
            ans += (y-x) * costs[2]
        else:
            ans += (x-y) * costs[4]
    elif x >= 0 and y <= 0:
        ans += x*costs[5]
        ans += abs(y)*costs[4]
    elif x <= 0 and y >= 0:
        ans += abs(x)*costs[2]
        ans += abs(y)*costs[1]
    print(ans)
