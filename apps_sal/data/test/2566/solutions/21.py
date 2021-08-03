import sys
import math
import bisect


def solve(A, first, m):
    ans = 0
    week_val = sum(A)
    #print('first: %d' % first)
    for i in range(first, 7):
        m -= A[i]
        ans += 1
        if m == 0:
            break
    #print('after the first week, m: %d, ans: %d' % (m, ans))
    if m > week_val:
        if m % week_val == 0:
            ans += 7 * (m // week_val - 1)
            m = week_val
        else:
            ans += 7 * (m // week_val)
            m %= week_val
    #print('after middle weeks, m: %d, ans: %d' % (m, ans))
    if m:
        for i in range(7):
            m -= A[i]
            ans += 1
            if m == 0:
                break
    #print('after the last week, m: %d, ans: %d' % (m, ans))
    return ans


def main():
    for _ in range(int(input())):
        m = int(input())
        A = list(map(int, input().split()))
        #print('A: %s, m: %d' % (str(A), m))
        min_val = 10 ** 18
        for i in range(7):
            val = solve(A, i, m)
            #print('first: %d, val: %d' % (i, val))
            min_val = min(min_val, val)
        print(min_val)


def __starting_point():
    main()


__starting_point()
