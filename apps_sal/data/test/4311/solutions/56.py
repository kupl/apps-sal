s = int(input())


def f(x):
    if x % 2 == 0:
        return int(x / 2)
    else:
        return 3 * x + 1


i = 1
m_max = 1000000
b_s = s
b = set([s])
while i <= m_max:
    i += 1
    a = f(b_s)
    if a in b:
        break
    b.add(a)
    b_s = a
print(i)
