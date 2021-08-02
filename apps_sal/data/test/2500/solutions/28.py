# coding: utf-8
# Your code here!
dic_memo = {0: 1, 1: 2}
M = 10**9 + 7


def memo(N):
    if N in dic_memo:
        return dic_memo[N]
    dic_memo[N] = (memo((N - 1) // 2) + memo(N // 2) + memo(N // 2 - 1)) % M
    return dic_memo[N]


n = int(input())
print((memo(n)))
