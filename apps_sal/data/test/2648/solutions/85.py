import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    cnt = 0
    for key, val in c.items():
        if val > 2:
            if val % 2 == 0:
                c[key] = 2
                cnt += 1
            else:
                c[key] = 1
        elif val == 2:
            cnt += 1
    
    if cnt % 2 == 0:
        print(len(c))
    else:
        print(len(c) - 1)


def __starting_point():
    main()
__starting_point()
