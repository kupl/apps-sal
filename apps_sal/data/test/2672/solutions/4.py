# your code goes here
n=int(input())
s=0
for i in range(1,4):
 s+=pow(n,i)
print(s%1000000007)
