"""
Created on Mon Sep  7 17:11:27 2020

@author: liang
"""
(N, M) = map(int, input().split())
ans = [-1] * N
res = 0
for i in range(M):
    (s, c) = map(int, input().split())
    if s == 1 and c == 0 and (N != 1):
        print(-1)
        break
    if ans[s - 1] == -1 or ans[s - 1] == c:
        ans[s - 1] = c
    else:
        print(-1)
        break
else:
    if ans[0] == -1:
        ans[0] = 1
    if M == 0 and N == 1:
        ans[0] = 0
    ans = [0 if a == -1 else a for a in ans]
    for i in range(N):
        res += ans[-(i + 1)] * 10 ** i
    print(res)
