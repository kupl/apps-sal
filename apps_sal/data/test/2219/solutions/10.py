t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    cnt = 0
    while n != 0:
        if n % k == 0:
            n //= k
            cnt += 1
        else:
            cnt += n % k
            n = n - n % k
    print(cnt)
