def f(t):
    n = t.count('#') - 1
    k = t.rfind('#') + 1
    t = t.replace('#', ')')
    t = [2 * ord(i) - 81 for i in t]

    a = b = c = 0
    for i in t[k:]:
        b -= i
        c -= i
        if c < 0: c = 0
    if c > 0: return -1
    for i in t[: k]:
        a -= i
        if a < 0: return -1

    if b + a < 0: return -1
    return '1\n' * n + str(b + a + 1)


print(f(input()))
