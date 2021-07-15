import sys
input = sys.stdin.readline

n=int(input())
E=[list(map(int,input().split())) for i in range(n-1)]

D=[0]*n

for x,y in E:
    D[x-1]+=1
    D[y-1]+=1

if 2 in D:
    print("NO")
else:
    print("YES")

