n,k,m = list(map(int,input().split()))
a = list(map(int,input().split()))
sum1 = sum(a)
stock = sum1
check = n*m
flag = 0
for i in range(k+1):
    sum1 += i
    if check <= sum1:
        ans = i
        flag = 1
        break
    sum1 = stock
if flag == 0:
    print((-1))
else:
    print(ans)

