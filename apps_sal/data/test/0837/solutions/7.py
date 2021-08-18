__author__ = 'Think'
n, x, y = [int(i) for i in input().split()]


def worth(num):
    if num % 2 == 0:
        dub = y
        alt = x * (num // 2)
    else:
        dub = y + x
        alt = x * ((num // 2) + 1)
    return dub < alt, dub, alt


time = 0
while n > 0:
    parity = n % 2
    should_double, dub, alt = worth(n)
    if should_double:
        time += dub
        if parity == 0:
            n = n // 2
            continue
        else:
            half = n // 2
            if half % 2 == 0:
                n = half
                continue
            else:
                if ((half // 2 + 1) * x + y) < half * x:
                    n = half + 1
                    continue
                else:
                    time += half * x
                    break
    else:
        time += n * x
        break

print(time)
