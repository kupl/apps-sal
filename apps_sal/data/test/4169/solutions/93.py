n,m = map(int,input().split())

l = [list(map(int,input().split())) for i in range(n)]

l.sort(key=lambda x: x[0])

r = m
i = 0
cnt = 0
while((r-l[i][1])>0):
    r -= l[i][1]
    cnt += (l[i][0]*l[i][1])
    i += 1

cnt += (r*l[i][0])

print(cnt)
