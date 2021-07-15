import sys
input = lambda : sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n,x=map(int,input().split())
    a = sorted([int(x) for x in input().split()])
    ans = 0
    while a and a[-1]>=x:
        ans +=1
        a.pop()
    i=len(a)-1
    l=1
    while i>=0:
        if a[i]*l>=x:
            ans += 1
            l=0
        i-=1
        l+=1
    print(ans)
