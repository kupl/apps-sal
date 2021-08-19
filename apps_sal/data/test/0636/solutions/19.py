import sys


def main():
    [k, n] = list(map(int, sys.stdin.readline().split()))
    instr_list = list(map(int, sys.stdin.readline().split()))
    arr1 = [(x, i + 1) for (i, x) in enumerate(instr_list)]
    arr2 = sorted(arr1)
    summ = 0
    res = []
    for (x, pos) in arr2:
        if summ + x > n:
            break
        else:
            summ += x
            res.append(pos)
    print(len(res))
    if res:
        print(' '.join(map(str, res)))


main()
