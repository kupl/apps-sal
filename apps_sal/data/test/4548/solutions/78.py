# -*- coding:utf-8 -*-
N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

A.append(X)
A.sort()

A_index = A.index(X)

len_bef = len(A[0:A_index])
len_aft = len(A[A_index + 1:])
ans = len_bef

if len_bef > len_aft:
    ans = len_aft

print(ans)
