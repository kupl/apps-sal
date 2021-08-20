t = int(input())
for i in range(t):
    ans = 0
    (n, k) = list(map(int, input().split()))
    while n != 0:
        if n % k == 0:
            n //= k
            ans += 1
        else:
            ans += n % k
            n -= n % k
    print(ans)
