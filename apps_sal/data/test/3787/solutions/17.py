import sys

input_methods = ['clipboard', 'file', 'key']
using_method = 1
input_method = input_methods[using_method]


def tin(): return map(int, input().split())
def lin(): return list(tin())


mod = 1000000007


def main():
    n, a, b = tin()
    if n < a + b - 1:
        return -1
    if n > a * b:
        return -1
    if a == 1:
        print(*list(range(n, 0, -1)))
        return
    if b == 1:
        print(*list(range(1, n + 1)))
        return

    al = list(range(1, n + 1))
    cc = (n - a) // (b - 1)
    amari = (n - a) % (b - 1)
    ret = al[-a:]
    st = n - a
    for bi in range(b - 1):
        na = cc + (1 if bi < amari else 0)
        st -= na
        for ai in range(na):
            ret.append(al[st + ai])
    print(*ret)


isTest = False


def pa(v):
    if isTest:
        print(v)


def input_clipboard():
    import clipboard
    input_text = clipboard.get()
    input_l = input_text.splitlines()
    for l in input_l:
        yield l


def __starting_point():
    if sys.platform == 'ios':
        if input_method == input_methods[0]:
            ic = input_clipboard()
            def input(): return ic.__next__()
        elif input_method == input_methods[1]:
            sys.stdin = open('inputFile.txt')
        else:
            pass
        isTest = True
    else:
        pass

    ret = main()
    if ret is not None:
        print(ret)


__starting_point()
