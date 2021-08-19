for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    n = a & b
    print((a ^ n) + (b ^ n))
