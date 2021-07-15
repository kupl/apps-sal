import sys
input = sys.stdin.readline

d={}
testnumber = int(input())

def calc(n, m, k):
    if k <= 0 or k == m*n:
        return 0
    if k > n*m:
        return 1000_000_000

    nonlocal d
    if n < m:
        n, m = m, n
    
    if k > (m*n - m):
        return m*m + 1
    if k < m:
        return m*m + 1
    if k % m == 0:
        return m*m

    if (n, m, k) in d:
        return d[ (n, m, k)]

    d[ (n, m, k) ] = min( calc2(n, m, k), calc2(m, n, k) )

    return d[ (n, m, k) ]

def calc2(n, m, k):
    m2 = m*m
    ans = m2*2 + 1
    for i in range(1, n):
        if i*m >= k:
            ans = min(ans, m2 + calc(m, i, k) )
        else:
            ans = min(ans, m2 + calc(m, n-i, k - i*m))
    
    return ans

for ntest in range(testnumber):
    n, m, k = map( int, input().split() )
    if k == n*m:
        print(0)
        continue

    print( calc(n, m, k) )
