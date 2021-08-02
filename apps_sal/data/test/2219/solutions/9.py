def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


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
