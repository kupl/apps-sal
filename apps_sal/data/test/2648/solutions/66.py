import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    for key, val in c.items():
        if val > 2:
            if val % 2 == 0:
                c[key] = 2
            else:
                c[key] = 1
    
    if len([val for key, val in c.items() if c[key] == 2]) % 2 == 0:
        print(len(c))
    else:
        print(len(c) - 1)


def __starting_point():
    main()
__starting_point()
