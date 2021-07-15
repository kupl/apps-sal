from sys import stdin, stdout # only need for big input
import numpy as np

def solve():
    s = input()
    n = len(s)
    ans = 1 
    for end in range(2,n,2):
        even = True
        for i in range(end//2):
            if s[i] != s[end//2 + i]:
                even = False
                break
        if even:
            ans = end
    print(ans)

def main():
    solve()


def __starting_point():
    main()
__starting_point()
