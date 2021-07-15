ii = lambda: int(input())
mi = lambda: list(map(int, input().split()))
li = lambda: list(mi())

for _ in range(ii()):
    n, k = mi()
    ans = 0
    while n:
        if n % k:
            ans += n % k
            n -= n % k
        else:
            ans += 1
            n //= k
    print(ans)

