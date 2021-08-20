for _ in range(int(input())):
    (n, k) = map(int, input().split())
    step = 0
    while n > 0:
        if n % k != 0:
            step += n % k
            n -= n % k
        else:
            while n % k == 0:
                n //= k
                step += 1
    print(step)
