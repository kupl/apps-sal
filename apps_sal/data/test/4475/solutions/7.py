"""T=int(input())
for _ in range(0,T):
    n=int(input())
    a,b=map(int,input().split())
    s=input()
    s=[int(x) for x in input().split()]
    for i in range(0,len(s)):
        a,b=map(int,input().split())"""
T = int(input())
for _ in range(0, T):
    (a, b, x, y, n) = list(map(int, input().split()))
    A = a
    B = b
    N = n
    d1 = a - x
    d2 = b - y
    t1 = min(d1, n)
    a -= t1
    n -= t1
    t2 = min(d2, n)
    b -= t2
    n -= t2
    ans = a * b
    d1 = A - x
    d2 = B - y
    t2 = min(d2, N)
    B -= t2
    N -= t2
    t1 = min(d1, N)
    A -= t1
    N -= t1
    ans = min(ans, A * B)
    print(ans)
