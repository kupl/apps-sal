n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
sum = 0
cnt = 0
for i in a:
    sum += i
for i in a:
    if(sum <= 4*m*i):
        cnt += 1
if(cnt >= m):
    print("Yes")
else:
    print("No")

