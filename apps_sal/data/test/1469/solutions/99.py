import sys
import math

input_methods = ['clipboard', 'file', 'key']
using_method = 1
input_method = input_methods[using_method]


def tin(): return list(map(int, input().split()))
def lin(): return list(IN())


mod = 1000000007


def main():
    L = int(input())
    v = int(math.log2(L))
    num_p = v
    path_info = []
    for i in range(v):
        path_info.append([i, i + 1, 0])
        path_info.append([i, i + 1, 2**i])

    nokori = L - (2 ** v)

    for i in range(v + 1):
        m = v - i
        if 2 ** m <= nokori:
            path_info.append([m, v, L - nokori])
            nokori -= 2 ** m
    print((v + 1, len(path_info)))
    for l in path_info:
        f, t, w = l
        print((*[f + 1, t + 1, w]))


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
