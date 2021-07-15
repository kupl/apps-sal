N,M=list(map(int,input().split()))

def primes(n):
    d=[]
    for i in range(1, int(n**0.5) + 1):
        if n%i==0:
            d.append(i)
            if n//i!=i:
                d.append(n//i)
    d.sort()
    return d

d=primes(M)

for i in d[::-1]:
    if M//i>=N:
        ans=i
        break

print(ans)

