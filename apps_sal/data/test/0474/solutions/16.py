import sys
inf = float('inf')
mod = 1000000007


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline()


def main():
    n = int(input())
    arr = get_array()
    maxi = max(arr)
    (mx, curr) = (0, 0)
    for i in range(n):
        if arr[i] == maxi:
            curr += 1
            mx = max(mx, curr)
        else:
            curr = 0
    print(mx)


def __starting_point():
    main()


__starting_point()
