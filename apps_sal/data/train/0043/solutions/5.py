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
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    low = 0
    high = max(a)
    ans = max(a)
    while low <= high:
        mid = low + high >> 1
        tot = 0
        for i in range(0, len(a)):
            if a[i] > mid:
                tot += b[i]
        if tot <= mid:
            ans = min(ans, mid)
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
