import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = input()
    right = 0
    left = 0
    for i in range(n):
        if S[i] == '(':
            left += 1
        elif left:
            left -= 1
        else:
            right += 1
    res = '(' * right + S + ')' * left
    print(res)


def __starting_point():
    resolve()


__starting_point()
