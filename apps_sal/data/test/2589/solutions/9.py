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
    (n, x) = list(map(int, input().split()))
    s = [int(x1) for x1 in input().split()]
    tot = 0
    for i in range(0, len(s)):
        tot += s[i]
    if tot % x != 0:
        print(n)
    else:
        ptr1 = 0
        ptr2 = 0
        c1 = 0
        c2 = 0
        for i in range(0, len(s)):
            if s[i] % x == 0:
                c1 += 1
            else:
                break
        for i in range(len(s) - 1, -1, -1):
            if s[i] % x == 0:
                c2 += 1
            else:
                break
        ans = n - min(c1, c2) - 1
        if ans == 0:
            print(-1)
        else:
            print(ans)
