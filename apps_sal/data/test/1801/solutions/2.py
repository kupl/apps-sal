
from math import sqrt,ceil,gcd
from collections import defaultdict



def modInverse(b,m):
    g = gcd(b, m)
    if (g != 1):
        # print("Inverse doesn't exist")
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)

def sol(n,m,rep):

    r = 1
    for i in range(2,n+1):
        j = i
        while j%2 == 0 and rep>0:

            j//=2
            rep-=1

        r*=j
        r%=m

    return r





def solve():

    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    m = int(input())
    hash = defaultdict(int)
    e = defaultdict(int)
    for i in range(n):
        hash[a[i]]+=1
        hash[b[i]]+=1
        if a[i] == b[i]:
            e[a[i]]+=1


    ans = 1
    for i in hash:

        z1 = hash[i]
        z2 = e[i]
        ans*=sol(z1,m,z2)
        ans%=m

    print(ans)





# t = int(input())
# for _ in range(t):
solve()




