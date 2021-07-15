#n = int(input())
a, b, x, y = list(map(int, input().split()))
#al = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#s=[list(map(int,input().split())) for i in range(n)]

if a == b:
    ans = x
else:
    dif = abs(a-b)
    if a < b:
        ans = x+min(2*x, y)*dif
    else:
        ans = x+min(2*x, y)*(dif-1)
print(ans)

