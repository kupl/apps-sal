import bisect
q=int(input())
ans=[]

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, int((n**0.5)//1+2)):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1] and is_prime[i//2]]
    return table

l_2017=sieve(10**5+1)[1:]

for i in range(q):
    l,r=map(int,input().split())
    ans.append(bisect.bisect_right(l_2017,r)-bisect.bisect_left(l_2017,l))

print(*ans,sep="\n")
