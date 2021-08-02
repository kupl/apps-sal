# 786
h, m = list(map(int, input().split(':')))


def rev(t):
    s = ''
    for c in reversed(t):
        s += c
    return s


def fun(hour, minute):
    sm, sh = '', ''
    if minute < 10:
        sm = '0' + str(minute)
    else:
        sm = str(minute)
    if hour < 10:
        sh = '0' + str(hour)
    else:
        sh = str(hour)
    return sh + sm


def is_palindrome(t):
    if rev(t) == t:
        return True
    return False


res = 0

while True:
    if is_palindrome(fun(h, m)):
        print(res)
        break
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    res += 1
