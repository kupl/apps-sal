def phi(n):
    t, i = n, 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            while n % i == 0: n //= i
            t -= t // i
        i += 1
    return t - t // n if n > 1 else t
print(phi(int(input()) - 1))
