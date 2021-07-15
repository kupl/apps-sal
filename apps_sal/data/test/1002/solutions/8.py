n, d = map(int,input().split())
t = list(map(int,input().split()))
sum = 0
for ti in t:
    sum += ti
if sum+(n-1)*10 <= d:
    print((d-sum)//5)
else:
    print(-1)
