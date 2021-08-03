a = input()
n = len(a)
b = ''
i = 0


def f(s):
    n = len(s)
    if len(set(s)) > 1:
        s1 = ''
        s1 += s[0]
        k = 1
        m = 1
        for i in range(1, n):
            if k == 1 and s1[-1] == s[i]:
                s1 += s[i]
                m += 1
            elif k == 1 and m == 1:
                s1 += s[i]
                k += 1
                m += 1
            else:
                s1 += ' '
                s1 += s[i]
                k = 1
                m = 1
        return s1
    return s


while i < n:
    s = ''
    s += a[i]
    i += 1
    while s[0] not in 'aeiou' and i < n and a[i] not in 'aeiou':
        s += a[i]
        i += 1
    s = f(s)
    b += s
print(b)
