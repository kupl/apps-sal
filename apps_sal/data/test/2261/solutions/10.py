def neg(a):
    if a == '+':
        return '*'
    else:
        return '+'


def gen(s, e, k, l, a):
    if s + 1 < e:
        mid = int((s + e) / 2)
        a[mid] = []
        for i in range(0, pow(2, l)):
            a[mid].append(a[s][i])
        for i in range(pow(2, l), pow(2, l + 1)):
            a[mid].append(neg(a[s][i]))
        for i in range(pow(2, l + 1), k):
            a[mid].append(a[mid][int(i % pow(2, l + 1))])
        gen(s, mid, k, l + 1, a)
        gen(mid, e, k, l + 1, a)
    return


def print_l(a, n):
    b = ''
    for i in range(0, n):
        b += str(a[i])
    print(b)
    return


n = int(input())
a = [None] * pow(2, n)
a[0] = ['+'] * pow(2, n)
gen(0, pow(2, n), pow(2, n), 0, a)
for i in range(0, pow(2, n)):
    print_l(a[i], pow(2, n))
