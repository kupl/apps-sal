# cook your dish here
n=int(input())
count=0
c=0
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0
count=0
for i in range(1,n+1):
    count=count+prime(i)
print(count)
