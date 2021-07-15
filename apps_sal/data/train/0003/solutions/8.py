t = int(input())
for _ in range(t):
    #n = int(input())
    n, k=map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s=0
    for i in range(k+1):
        s+=a[n-1-i]
    print(s)
