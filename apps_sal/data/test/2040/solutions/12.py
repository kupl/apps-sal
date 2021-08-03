def min_number(sum_digits):
    res = 0
    base = 1
    while sum_digits > 9:
        res += 9 * base
        base *= 10
        sum_digits -= 9
    res += sum_digits * base
    return res


def from_digits(d):
    res = 0
    base = 1
    for digit in d:
        res += digit * base
        base *= 10
    return res


def next_number(x, sum_digits):
    if min_number(sum_digits) > x:
        return min_number(sum_digits)

    sd = sum_digits
    x_digits = []
    while x:
        x_digits.append(x % 10)
        x //= 10

    if sum_digits > sum(x_digits):
        res_digits = x_digits[::]
        i = 0
        while sum(res_digits) < sum_digits:
            while res_digits[i] == 9:
                i += 1
            res_digits[i] += 1
        return from_digits(res_digits)

    x_digits.append(0)
    d = x_digits[::-1]

    res_digits = [0] * len(d)
    last_incable = 0
    for i in range(0, len(d)):
        if sum_digits > d[i]:
            res_digits[i] = d[i]
            sum_digits -= d[i]
            if d[i] != 9:
                last_incable = i
        else:
            break

    d[last_incable] += 1
    for i in range(last_incable + 1, len(d)):
        d[i] = 0
    rest = sd - sum(d)
    res = from_digits(d[::-1]) + min_number(rest)
    return res


def solve(b):
    r = min_number(b[0])
    print(r)
    for i in range(1, len(b)):
        r = next_number(r, b[i])
        print(r)


n = int(input())
b = [0] * n
for i in range(0, n):
    b[i] = int(input())

solve(b)
