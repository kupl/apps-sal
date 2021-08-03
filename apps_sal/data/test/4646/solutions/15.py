"""
Author: Q.E.D
Time: 2020-06-16 09:39:00
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    odd = 0
    even = 0
    for i, x in enumerate(a):
        if i % 2 == 1 and x % 2 == 0:
            odd += 1
        elif i % 2 == 0 and x % 2 == 1:
            even += 1
    if odd == even:
        ans = odd
    else:
        ans = -1
    print(ans)
