import math
sum_ = [0] * 18
begin_ = [0] * 18


def f_(x0, k, n):
    return k * (2 * x0 + (k - 1) * n) // 2


def make():
    x0 = 1
    k = 9
    n = 1
    while n < 18:
        begin_[n] = x0
        last_number = x0 + (k - 1) * n
        sum = k * (2 * x0 + (k - 1) * n) // 2
        sum_[n] = sum
        sum_[n] += sum_[n - 1]
        x0 = last_number + (n + 1)
        k *= 10
        n += 1


def digit(x):
    cnt = 0
    while x > 0:
        x //= 10
        cnt += 1
    return cnt


def f(x, begin_, sum_):
    n = digit(x)
    k = x - 10 ** (n - 1) + 1
    x0 = begin_[n]
    return sum_[n - 1] + f_(x0, k, n)


def find(s, begin_, sum_):
    l = 0
    u = 1000000000
    while u - l > 1:
        md = (l + u) // 2
        if f(md, begin_, sum_) > s:
            u = md
        else:
            l = md
    return (l, s - f(l, begin_, sum_))


def get_digit(x, pos):
    s = []
    while x > 0:
        s.append(x % 10)
        x //= 10
    return s[::-1][pos]


def find_digit(x):
    (pos, remain) = find(x, begin_, sum_)
    if remain == 0:
        return pos % 10
    n = 0
    next_ = 9 * 10 ** n * (n + 1)
    while next_ <= remain:
        remain -= next_
        n += 1
        next_ = 9 * 10 ** n * (n + 1)
    if remain == 0:
        return 9
    pos_ = 10 ** n + math.ceil(remain / (n + 1)) - 1
    return get_digit(pos_, (remain - 1) % (n + 1))


make()
q = int(input())
for _ in range(q):
    n = int(input())
    print(find_digit(n))
