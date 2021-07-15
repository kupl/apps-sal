import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())
ans=0

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

ndivs = make_divisors(n)

n1divs = make_divisors(n-1)
ans += len(n1divs)-1

for i in range(1,len(ndivs)):
    tmp = n
    k = ndivs[i]
    while tmp%k==0:
        tmp //=k
    if tmp%k==1:ans+=1

print(ans)

