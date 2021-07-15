import sys
import math
import bisect

def query_value(A, a, r, m, target):
    n = len(A)
    more_val = 0
    less_val = 0
    for i in range(n):
        if A[i] > target:
            more_val += A[i] - target
        elif A[i] < target:
            less_val += target - A[i]
    move_val = min(more_val, less_val)
    val1 = more_val * r + less_val * a
    val2 = (more_val - move_val) * r + (less_val - move_val) * a + (move_val) * m
    '''
    print('n: %d, a, %d, r: %d, m: %d' % (n, a, r, m))
    print('more_val: %d, less_val: %d, move_val: %d' % (more_val, less_val, move_val))
    print('val1: %d' % (val1))
    print('val2: %d' % (val2))
    print('target: %d, val: %d' % (target, min(val1, val2)))
    '''
    return min(val1, val2)

def main():
    n, a, r, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    left = min(A)
    right = max(A)
    while right - left > 2:
        #print('left: %d, right: %d' % (left, right))
        m1 = left + (right - left) // 3
        m2 = left + (right - left) // 3 * 2
        val1 = query_value(A, a, r, m, m1)
        val2 = query_value(A, a, r, m, m2)
        if val1 <= val2:
            right = m2
        else:
            left = m1
    B = []
    for i in range(left, right + 1):
        val = query_value(A, a, r, m, i)
        B.append(val)
    print(min(B))

def __starting_point():
    main()

__starting_point()
