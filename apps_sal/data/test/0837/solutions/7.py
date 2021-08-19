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
            # print("Doubled, even,", n, n//2, time)
            n = n // 2
            continue
        else:
            half = n // 2
            if half % 2 == 0:
                # print("Doubled, 1 mod 4,", n, half, time)
                n = half
                continue
            else:
                if ((half // 2 + 1) * x + y) < half * x:
                    # print("Doubled, 3 mod 4, continued", n, half+1, time)
                    n = half + 1
                    continue
                else:
                    # print("Doubled, 3 mod 4, end", n, half, time)
                    time += half * x
                    break
    else:
        # print("Haven't doubled, ", n, time)
        time += n * x
        break

print(time)
