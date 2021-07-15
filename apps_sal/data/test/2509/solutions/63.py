n, k = list(map(int, input().split()))

s = 0

if k == 0:
    print(n ** 2)
else:
    for i in range(k+1, n+1):
        if n % i < k:
            s += n // i * (i - k)
        else:
            s += n // i * (i - k) + n % i - (k-1)
        
    print(s)
