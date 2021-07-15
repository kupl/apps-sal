N,K = map(int,input().split())

ans = 0
for n in range(1,N+1):
    k = 0
    m = n
    while m < K:
        m *= 2
        k += 1
    ans += 2**(-k)
print(ans / N)
