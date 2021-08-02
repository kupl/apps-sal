s = input()


def f(a):
    a = a.lower()
    a = a.replace('o', '0')
    a = a.replace('i', '1')
    a = a.replace('l', '1')
    return a


s = f(s)
q = int(input())
b = True
for i in range(0, q):
    d = input()
    if s == f(d):
        b = False
print('Yes' if b else 'No')
