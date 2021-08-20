while True:
    try:
        (n, t, k, d) = list(map(int, input().split()))
        from math import ceil
        print('YES' if ceil(n / k) * t > t + d else 'NO')
    except EOFError:
        break
