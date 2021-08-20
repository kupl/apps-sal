"""
Created on Wed Sep 30 00:56:12 2020

@author: liang
"""
(N, M) = map(int, input().split())
if N * 2 >= M:
    print(M // 2)
else:
    print(N + (M - 2 * N) // 4)
