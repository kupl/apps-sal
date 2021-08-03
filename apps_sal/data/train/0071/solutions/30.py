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
    n = int(input())
    s = [int(x) for x in input().split()]
    nrem = 0
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        if(s[i] > 0):
            tt = min(nrem, s[i])
            s[i] -= tt
            ans += s[i]
            nrem -= tt
        else:
            nrem += abs(s[i])

    print(ans)
