def foo(n):
    a = []
    s = []
    leng = 0
    last_leng = 0
    for i in range(1, n + 1):
        for c in str(i):
            last_leng += 1
        leng += last_leng
    return leng


def small_foo(n):
    leng = 0
    for i in range(1, n + 1):
        leng += len(str(i))
    return leng


def bar(n):
    total_len = 0
    for i in range(1, len(str(n))):
        max_i_digit = 10 ** i - 1
        i_digit_num = 9 * 10 ** (i - 1)
        start_count = i_digit_num * (i_digit_num + 1) // 2
        end_count = i_digit_num * (n - max_i_digit)
        i_digit_total_len = (start_count + end_count) * i
        total_len += i_digit_total_len
    i = len(str(n))
    i_digit_num = n - (10 ** (i - 1) - 1)
    start_count = i_digit_num * (i_digit_num + 1) // 2
    total_len += start_count * i
    return total_len


def small_bar(n):
    total_len = 0
    for i in range(1, len(str(n))):
        i_digit_num = 9 * 10 ** (i - 1)
        total_len += i_digit_num * i
    i = len(str(n))
    i_digit_num = n - (10 ** (i - 1) - 1)
    total_len += i_digit_num * i
    return total_len


def small_solve(x, n):
    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if small_bar(m) >= x:
            r = m
        else:
            l = m
    return str(r)[x - small_bar(l) - 1]


def solve(x):
    l = 0
    r = 10 ** 9
    while r - l > 1:
        m = (l + r) // 2
        if bar(m) >= x:
            r = m
        else:
            l = m
    return small_solve(x - bar(l), r)


def main():
    q = int(input())
    for _ in range(q):
        x = int(input())
        print(solve(x))


main()
