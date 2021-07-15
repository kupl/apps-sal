import sys
from math import ceil


def main():
    n, s = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    if s > sum(arr):
        print(-1, sep=' ', end='\n', file=sys.stdout, flush=False)
    else:
        count = 0
        arr.sort(reverse=True)
        for i in range(n-1):
            if count == s:
                break
            if count+(arr[i]-arr[-1]) <= s:
                count += arr[i]-arr[-1]
                arr[i] = arr[-1]
            elif count+(arr[i]-arr[-1]) > s:
                count = s
                arr[i] -= (s-count)
        if count == s:
            print(arr[-1])
        else:
            factor = (s-count)/n

            print(arr[-1]-ceil(factor), sep=' ', end='\n', file=sys.stdout, flush=False)


def __starting_point():
    main()

__starting_point()
