n, x0, y0 = map(int, input().split())

ps = [list(map(int, input().split())) for i in range(n)]

shut = [False for i in range(n)]

ans=i=0

for x,y in ps:
    if not shut[i]:
        ans+=1
        j=0
        for x2, y2 in ps:
            if (x-x0)*(y2-y0) == (x2-x0)*(y-y0):
                shut[j]=True
            j+=1
    i+=1

print(ans)
