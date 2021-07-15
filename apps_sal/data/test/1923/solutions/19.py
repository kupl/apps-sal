n=int(input())
l=sorted(list(map(int,input().split())))
sum=0
for i in range(2*n):
    if i%2==0:
        sum+=l[i]
print(sum)
