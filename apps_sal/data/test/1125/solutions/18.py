def f_unfair_nim():
    from functools import reduce
    from operator import xor
    N = int(input())
    A = [int(i) for i in input().split()]

    s = sum(A[:2])
    x = reduce(xor, A[2:], 0)
    if (s - x) % 2 != 0 or (((s - x) // 2) & x) != 0:
        return -1

    a = (s - x) // 2
    for i in range(60, -1, -1):
        if (x & (1 << i)) != 0 and (a ^ (1 << i) <= A[0]):
            a ^= 1 << i
    return A[0] - a if A[0] >= a > 0 else -1

print(f_unfair_nim())
