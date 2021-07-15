from bisect import *

n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for b in B:
    index_A = bisect_left(A, b)
    index_C = bisect_right(C, b)
    ans += index_A * (n - index_C)
print(ans)
