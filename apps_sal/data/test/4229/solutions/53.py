N=int(input())

sum=0
i=1
while i<=N:
    if i%3!=0 and i%5!=0:
        sum=sum+i
    i=i+1

print(sum)

