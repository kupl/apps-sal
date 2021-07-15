from sys import stdin 

n = int(stdin.readline())

size = list(map(int,stdin.readline().split()))
price = list(map(int,stdin.readline().split()))

temp = [3*10**8 + 1] * n
ans = [3*10**8 + 1] * n

for i in range(n):
    for j in range(i+1,n) :
        if (size[i] >= size[j]) :
            continue
        temp[j] = min(temp[j],price[i]+price[j])
for i in range(n):
    for j in range(i+1,n):
        if(size[i] >= size[j]):
            continue
        ans[j] = min(ans[j],temp[i]+price[j])
res = 3*10**8 + 1
for i in range(n):
    if (res > ans[i]) :
        res = ans[i]
if (res == 3*10**8 + 1):
    print("-1")
else :
    print(res)




