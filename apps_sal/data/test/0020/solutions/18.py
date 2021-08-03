h, m = [int(x) for x in input().split(":")]
ans = 0


def padL(s):
    while len(s) < 2:
        s = '0' + s
    return s


def palindrome():
    t = padL(str(h)) + padL(str(m))
    return t == t[::-1]


while not palindrome():
    m += 1
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
    ans += 1
print(ans)
