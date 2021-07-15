a,b = map(int,input().split())

List = []
for i in range(2,61):
    for j in range(i-2,-1,-1):
        List+=[(1<<i)-(1<<j)-1]

res = 0
for i in List:
    if a<=i and i<=b: res+=1

print(res)
