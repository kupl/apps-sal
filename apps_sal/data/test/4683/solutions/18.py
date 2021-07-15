n = int(input())
arr = input()
ar = list(map(int,arr.split(' ')))
sum=0
s=0
mod=1000000007
for i in range(0,n):
    sum=sum+(ar[i]*ar[i])
    s=s+ar[i]
s=s*s
print(((s-sum)//2)%mod)
