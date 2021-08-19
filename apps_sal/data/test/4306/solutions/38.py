# -*- coding: utf-8 -*-

A, B, C, D = map(int, input().split())

start = max(A, C)
end = min(B, D)
ans = max(end - start, 0)
print(ans)
