from fractions import gcd
g=lambda a,b:a//gcd(a,b)*b
n=int(input())+1
m=max(1,n-50)
print(max([g(a,g(b,c))for a in range(m,n)for b in range(m,n) for c in range(m,n)]))
