n,x,y = list(map(int,input().split()))

ans = [0]*n
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if i <= x and j >= y:
            a = abs(j-i)-abs(y-x)+1
            b = abs(i-x)+abs(j-y)+1
            ans[min(a,b)] += 1
        else:
            c = abs(x-i)+abs(y-j)+1
            d = abs(j-i)
            ans[min(c,d)] += 1

for i in range(1,n):
    print((ans[i]))

