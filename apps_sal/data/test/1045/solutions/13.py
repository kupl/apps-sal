#Codeforces #492 problem A
n=int(input())
i=1
sum=1

while n>sum:
    i+=1
    sum+=(i*(i+1))/2

if n<sum:
    i-=1

print(i)

