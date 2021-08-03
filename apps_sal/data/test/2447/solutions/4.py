"""
Author: Q.E.D
Time: 2020-05-31 09:41:24
"""
T = int(input())
for _ in range(T):
    s = input()
    one = [0]
    zero = [0]
    for i, c in enumerate(s):
        if c == '0':
            zero.append(zero[-1] + 1)
            one.append(one[-1])
        else:
            one.append(one[-1] + 1)
            zero.append(zero[-1])
    n = len(s)
    ans = n
    for i in range(1, n + 1):
        ans = min(ans, zero[i] + one[n] - one[i])
        ans = min(ans, one[i] + zero[n] - zero[i])
    print(ans)
