import sys
import math
from collections import defaultdict
from collections import deque
from itertools import combinations
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def read():
    return list(map(int, input().split()))


def go():
    return 1 / 0


def write(*args, sep='\n'):
    for i in args:
        sys.stdout.write('{}{}'.format(i, sep))


INF = float('inf')
MOD = int(1000000000.0 + 7)
YES = 'YES'
NO = 'NO'
for _ in range(int(input())):
    try:
        n = int(input())
        arr = read()
        ans = 0
        for i in range(n):
            if arr[i] == 0:
                arr[i] = 1
                ans += 1
        if sum(arr) == 0:
            print(ans + 1)
        else:
            print(ans)
    except ZeroDivisionError:
        continue
    except Exception as e:
        print(e)
        continue
