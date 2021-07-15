import sys


def get_sn():
    return int(input())

def get_n():
    return list(map(int, input().split()))

def get_ln():
    return list(get_n())

def cond(x, a, n):
    for i in range(n - x + 1):
        if len(set(a[:i] + a[i + x:])) == n - x:
            return True
    return False

def solve(a, n):
    l, r = -1, n + 1
    while r - l > 1:
        m = (r + l) // 2
        if cond(m, a, n):
            r = m
        else:
            l = m
    return r

def main():
    n = get_sn()
    arr = get_ln()
    print(solve(arr, n))

main()

