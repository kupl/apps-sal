a,b,k=[int(num) for num in input().split()]
count=[]
c=min(a,b)
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        count.append(i)
print(count[-k])
