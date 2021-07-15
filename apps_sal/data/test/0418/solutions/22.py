"""a,b,n,x = map(int,input().split())
list(map(int,input().split()))
[list(map(int,input().split())) for i in range(n)]"""
n = int(input())
nbai = [list(map(str,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    if int(nbai[i][2]) > int(nbai[i][1]) and int(nbai[i][1]) > 2399:
        ans = 1
        break
if ans == 1:
    print("YES")
else:
    print("NO")

        

