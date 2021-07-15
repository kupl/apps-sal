3

k, n, m = list(map(int, input().split()))

wa = n // k
wb = m // k

if n % k > 0 and wb == 0:
    print(-1)
elif m % k > 0 and wa == 0:
    print(-1)
else:
    print(wa + wb)

