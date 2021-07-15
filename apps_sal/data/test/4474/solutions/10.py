
q = int(input())
N = [int(input()) for i in range(q)]
t = [3**i for i in range(10)]

def d(x):
    ans = 0
    m = 1
    while x > 0:
        if x % 2 == 1:
            ans += m
        m *= 3
        x //= 2
    return(ans)

# print(d(2))


for i in range(q):
    n = N[i]
    m = 0
    t = 0
    l = 0
    r = 2**50
    mid = (l+r)//2
    while r - l > 1:
        
        m = d(mid)
        if m >= n:
            r = mid
        else:
            l = mid
        mid=(l+r)//2

    print(d(l+1))




