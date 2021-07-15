n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]
 
l = sorted(l, key = lambda x:(x[1], x[0]))
cnt = m
 
for i in range(1, m):
    if l[i-1][1] > l[i][0]:
        l[i][1] = l[i-1][1]
        cnt -= 1
 
print(cnt)
