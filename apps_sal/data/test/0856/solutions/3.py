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
    (n, k) = list(map(int, input().split()))
    s = [int(x) for x in input().split()]
    kk = max(s)
    for i in range(0, len(s)):
        s[i] = kk - s[i]
    k -= 1
    if k % 2 == 0:
        print(*s)
    else:
        kk = max(s)
        for i in range(0, len(s)):
            s[i] = kk - s[i]
        print(*s)
