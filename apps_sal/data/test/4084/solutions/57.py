# -*- coding:utf-8 -*-
N, A, B = map(int, input().split())

apb = A + B
ans = A * (N // apb)
N = N % apb

if N > A:
    ans += A
else:
    ans += N
print(ans)
