t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    f=False
    for i in range(n-1):
        if a[i]<=a[i+1]:
            f=True
    if f:
        print('YES')
    else:
        print('NO')
