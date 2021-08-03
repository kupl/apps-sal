N, K = map(int, input().split())
A = list(map(int, input().split()))
t = 2**40
ans = 0

while t:
    c = sum([(A[n] & t) // t for n in range(N)])
    if K < t or c * 2 >= N:
        ans += t * c
    else:
        ans += t * (N - c)
        K -= t
    t //= 2

print(ans)
