from math import factorial as f
def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
p = primes(31627)
s = [0]*(31623)
s1={}
def factorize(n):
  for i in p:
    if n<=1:
      return 56
    while n%i==0:
      s[p.index(i)]+=1
      n//=i
  if n>1:
    if n in s1:
      s1[n]+=1
    else:
      s1[n]=1
n = int(input())
for i in map(int,input().split()):
  factorize(i)
s = list(filter(lambda a: a != 0, s))
for i in s1.values():
  s.append(i)
ans = 1
for i in s:
  ans*=f(i+n-1)//(f(n-1)*f(i))
print(int(ans)%1000000007)
