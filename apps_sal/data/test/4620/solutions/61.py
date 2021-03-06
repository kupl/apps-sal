import sys
input_methods = ['clipboard', 'file', 'key']
using_method = 0
input_method = input_methods[using_method]


def tin():
    return map(int, input().split())


def lin():
    return list(tin())


mod = 1000000007


def cc(al):
    ret = 0
    for (c, s, f) in al:
        if ret <= s:
            ret = s + c
        else:
            st = (ret + f - 1) // f * f
            ret = st + c
    print(ret)


def main():
    n = int(input())
    al = [lin() for _ in range(n - 1)]
    for i in range(n):
        cc(al[i:])


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

            def input():
                return ic.__next__()
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
