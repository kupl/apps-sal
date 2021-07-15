h,w,d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]
b = [0]*(h*w+1)
for i in range(h):
    for j in range(w):
        b[a[i][j]] = (i,j)
#print(b)
ans = [0]*(h*w+1)
for i in range(d+1,h*w+1):
    ans[i] = ans[i-d]+abs(b[i][0]-b[i-d][0])+abs(b[i][1]-b[i-d][1])
#print(ans)
for i in range(q):
    x,y = lr[i][0],lr[i][1]
    print(ans[y]-ans[x])
