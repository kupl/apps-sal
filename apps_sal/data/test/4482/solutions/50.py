n=int(input())
a=list(map(int,input().split()))
# n=2
# a=[4,8]
minimum=10000000
for i in range(-100,101):
    cost=0
    for j in range(n):
        cost+=(i-(a[j]))**2
        if j==n-1:
            if cost<minimum:
                minimum=cost

print(minimum)



