import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations
def input(): return sys.stdin.readline().rstrip()
def read(): return list(map(int, input().split()))
def go(): return 1 / 0


def write(*args, sep="\n"):
    for i in args:
        sys.stdout.write("{}{}".format(i, sep))


INF = float('inf')
MOD = int(1e9 + 7)
YES = "YES"
NO = "NO"

for _ in range(int(input())):
    try:
        a, b, p = read()
        s = input()

        stack = [[s[0], 1]]

        for i in s[1:-1]:
            if i == stack[-1][0]:
                stack[-1][1] += 1

            else:
                stack.append([i, 1])

        ans = len(s)
        temp = []
        # print(stack)

        if p < a and p < b:
            print(len(s))
            go()

        while stack:
            i, j = stack[-1]
            stack.pop()
            if i == 'A' and p >= a:
                p -= a
                ans -= j
                temp.append(j)
            elif i == 'A' and p < a:
                break
            if i == 'B' and p >= b:
                p -= b
                ans -= j
                temp.append(j)
            elif i == 'B' and p < b:
                break

        print(ans)

    except ZeroDivisionError:
        continue

    except Exception as e:
        print(e)
        continue
