n = int(input())
x = list(map(int,input().split()))
ans = float('inf')
for i in range(min(x),max(x)+1):
    dist = 0
    for j in x:
        dist += (j-i) ** 2
    ans = min(ans,dist)
print(ans)
