def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
    
n = int(input())
a = [int(x) for x in input().split()]
sum1 = sum(a)
sum2 = 0
sumbefore = 0
a.sort()
for i in range(n):
    sum2 += a[i]*(i) - sumbefore
    sumbefore += a[i]
sumtot = sum1 + 2*sum2
k = gcd(sumtot,n)
print(sumtot//k,n//k)
