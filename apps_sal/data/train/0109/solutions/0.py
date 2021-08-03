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
NO = -1

for _ in range(int(input())):
    try:
        n, m = read()
        arr = read()
        x = [0] * 65

        if sum(arr) < n:
            print(NO)
            go()

        for i in arr:
            x[int(math.log2(i))] += 1

        ans = 0
        for i in range(65):
            if (1 << i) & n:
                if x[i] != 0:
                    x[i] -= 1
                    continue

                total = 0
                for j in range(i):
                    total += (1 << j) * x[j]

                if total >= (1 << i):
                    temp = 1 << i
                    for j in reversed(range(i)):
                        while temp - (1 << j) >= 0 and x[j] > 0:
                            temp -= 1 << j
                            x[j] -= 1
                    continue

                j = i
                while j < 65 and x[j] == 0:
                    j += 1
                if j == 65:
                    print(NO)
                    go()
                else:
                    x[j] -= 1
                    for k in range(i, j):
                        x[k] += 1
                    ans += (j - i)

        print(ans)

    except ZeroDivisionError:
        continue

    except Exception as e:
        print(e)
        continue
