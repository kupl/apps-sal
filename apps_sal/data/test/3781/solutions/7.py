import sys
from collections import defaultdict
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり


T = I()
for _ in range(T):
    N = I()
    A = LI()
    if N % 2 == 1:
        print('Second')
    else:
        d = defaultdict(int)
        for a in A:
            d[a] += 1
        X = list(d.values())
        for x in X:
            if x % 2 == 1:
                print('First')
                break
        else:
            print('Second')
