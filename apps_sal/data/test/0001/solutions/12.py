
def e(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def down(x):
    l = len(x) - 1
    return str(int(x[0]) - 1) + '9' * l


n = input()
if len(n) > 1 and n[1] == '9':
    print(n[0], end='')
    n = n[1:]
    while len(n) > 1 and n[0] == '9' and n[1] == '9':
        print('9', end='')
        n = n[1:]

if e(int(n)) >= e(int(down(n))):
    print(n)
else:
    print(int(down(n)))
