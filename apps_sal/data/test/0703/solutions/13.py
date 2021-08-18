max_parts, n, divisors, nuts_in_part = map(int, input().split())
L = 0
R = 10000
while R - L > 1:
    M = (L + R) // 2
    available_divisors = min(M * (max_parts - 1), divisors)
    if (M + available_divisors) * nuts_in_part >= n:
        R = M
    else:
        L = M

available_divisors = min(L * (max_parts - 1), divisors)
if (L + available_divisors) * nuts_in_part >= n:
    print(L)
else:
    print(R)
