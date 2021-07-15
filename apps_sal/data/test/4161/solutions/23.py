import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    k = int(input())

    k2 = np.arange(1, k+1)
    k2gcd = np.gcd.outer(k2, np.gcd.outer(k2, k2))
    print(k2gcd.sum())

def __starting_point():
    main()
__starting_point()
