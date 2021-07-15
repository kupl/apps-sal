"""
Author: Q.E.D
Time: 2020-09-06 09:35:20
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    print(' '.join(map(str, a[::-1])))
