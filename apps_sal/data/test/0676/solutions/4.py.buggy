'''
x1 + x2 + x3 + x4 = 4 * x
x1 + x4 = 2 * x
x4 - x1 = x

x1 = 0.5 * x
x2 + x3 = 2 * x
x4 = 1.5 * x
'''

import itertools


def check(*xs):

    return sum(xs) == 2 * sum(xs[1:3]) == 4 * (xs[-1] - xs[0]) and all([0 < x <= 10 ** 6 for x in xs]) and tuple(sorted(xs)) == xs


def solve(x1=None, x2=None, x3=None, x4=None):

    x = None
    if x1 is not None:

        x = 2 * x1
        if x4 is not None and 3 * x1 != x4:

            return

        x4 = 3 * x1

    if x4 is not None:

        if 2 * x4 % 3 != 0:

            return

        x = 2 * x4 // 3
        if x1 is not None and x // 2 != x1:

            return

        x1 = x // 2

    if x is None:

        if (x2 + x3) % 2 != 0:

            return

        x = (x2 + x3) // 2
        if x % 2 != 0:

            return

        x1 = x // 2
        x4 = 3 * x1

    else:

        if x2 is not None and x3 is None:

            x3 = 2 * x - x2

        elif x3 is not None and x2 is None:

            x2 = 2 * x - x3

    if check(x1, x2, x3, x4):

        return x1, x2, x3, x4


n = int(input())
if n == 0:

    print("YES")
    print(str.join("\n", list(map(str, (1, 1, 3, 3)))))

elif n == 1:

    a = int(input())
    print("YES")
    print(str.join("\n", [str(x * a) for x in (1, 3, 3)]))

elif n == 4:

    a = []
    for _ in range(n):

        a.append(int(input()))

    print("YES" if check(*sorted(a)) else "NO")

else:

    a = [None] * 4
    for i in range(n):

        a[i] = int(input())

    for comb in itertools.permutations(a, 4):

        nums = list(filter(bool, comb))
        if nums != sorted(nums):

            continue

        r = solve(*comb)
        if r is not None:

            print("YES")
            for x, xc in zip(r, comb):

                if xc is None:

                    print(x)

            return

    else:

        print("NO")
