n = int(input())


def get_sum(x):
    result = 0
    while x > 0:
        d, m = divmod(x, 10)
        result += m
        x = d
    return result


def dec(x):
    assert x != 0
    t = x
    mult = 1
    while True:
        d, m = divmod(x, 10)
        if m != 0:
            return t + (10 - m) * mult
        x = d
        mult *= 10


def get_next(prev_x, prev_sum, sum):
    t = prev_x
    while True:
        while prev_sum > sum:
            prev_x = dec(prev_x)
            prev_sum = get_sum(prev_x)
        s = list(reversed(str(prev_x)))
        required = sum - prev_sum
        i = 0
        while required:
            try:
                a = min(9 - (ord(s[i]) - ord('0')), required)
                s[i] = chr(ord(s[i]) + a)
            except IndexError:
                a = min(9, required)
                s += chr(a + ord('0'))
            required -= a
            i += 1
        x = int("".join(reversed(s)))
        if x != t:
            return x
        prev_x = dec(prev_x)
        prev_sum = get_sum(prev_x)


a = s = 0
for i in range(n):
    b = int(input())
    a = get_next(a, s, b)
    print(a)
    s = b
