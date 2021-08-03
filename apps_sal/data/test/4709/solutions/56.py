'''
ABC050 A - Addition and Subtraction Easy
https://atcoder.jp/contests/abc050/tasks/abc050_a
'''


def main():
    a, op, b = input().split()
    a, b = int(a), int(b)

    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    print(ans)


def __starting_point():
    main()


__starting_point()
