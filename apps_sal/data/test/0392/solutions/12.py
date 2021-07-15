def Factor(n):
    Ans = 1
    d = 2
    used = []
    while d * d <= n:
        if n % d == 0:
            if d not in used:
                Ans *= d
                used.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        if n not in used:
            Ans *= n
    return Ans

print(Factor(int(input())))

