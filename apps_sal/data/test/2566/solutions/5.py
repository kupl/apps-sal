# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 12/3/18

"""


def solve(k, a):
    w = sum(a)
    ans = float('inf')
    if k <= w:
        for start in range(7):
            for end in range(start, 8):
                if sum(a[start: end]) >= k:
                    ans = min(ans, end - start)

    for start in range(7):
        for end in range(7):
            x = sum(a[start:])
            y = sum(a[:end + 1])
            z = k - x - y
            if z >= 0 and z % w == 0:
                ans = min(ans, z // w * 7 + end + 1 + 7 - start)
    return ans


T = int(input())
ans = []
for ti in range(T):
    K = int(input())
    A = [int(x) for x in input().split()]
    ans.append(solve(K, A))

print('\n'.join(map(str, ans)))
