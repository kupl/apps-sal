# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n = int(input())
a = list(map(int, input().split()))
a2 = [ai - i for i, ai in enumerate(a, 1)]

a2.sort()
cumsum = [0] * n
cumsum[0] = a2[0]
for i in range(n - 1):
    cumsum[i + 1] = cumsum[i] + a2[i + 1]

ans = 10**20
for i in range(n):
    low = cumsum[i]
    high = cumsum[-1] - cumsum[i]
    ai = a2[i]
    ans = min(ans, (ai * (i + 1) - low) + (high - ai * (n - 1 - i)))
print(ans)
