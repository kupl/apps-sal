def f():
    n = int(input()) // 3
    t = input()
    if '5' in t:
        return -1
    a = t.count('1')
    if a != n:
        return -1
    b = t.count('2')
    c = t.count('3')
    if b + c != n:
        return -1
    d = t.count('4')
    if d > b:
        return -1
    f = t.count('6')
    if f < c:
        return -1
    return '1 2 4\n' * d + '1 3 6\n' * c + '1 2 6\n' * (n - d - c)


print(f())
