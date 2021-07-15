n, k = map(int, input().split())

if k > n+n-1:
    print(0)
    return

if k <= n:
    print((k-1)//2)
    return

print((n+n-k+1)//2)
