n=int(input())
a=27
b=20
for i in range(2,n+1):
    b=(1000000007+a*20+b*27-b*20)%1000000007
    a=a*27%1000000007
print(b)
