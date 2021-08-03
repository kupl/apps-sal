from bisect import *
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for b in B:
    ans += (n - bisect(C, b)) * bisect_left(A, b)
print(ans)
