
n = int(input())


def get_divisors(num):
    if num == 1:
        return [1]

    divisors = []
    for d in range(1, num):
        if d * d > num:
            break
        if num % d == 0:
            divisors.append(d)
            if d * d != num:
                divisors.append(int(num // d))

    return divisors


ans = len(get_divisors(n - 1)) - 1

for divisor in get_divisors(n):
    if divisor == 1:
        continue
    temp = n
    while(True):
        if temp % divisor != 0:
            break
        temp = temp // divisor

    if temp % divisor == 1:
        ans += 1

print(ans)
