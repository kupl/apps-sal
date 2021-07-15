"""
Author: Q.E.D
Time: 2020-06-16 09:36:16
"""
T = int(input())
for _ in range(T):
    b = input()
    a = b[0] + b[1:-1:2] + b[-1]
    print(a)
