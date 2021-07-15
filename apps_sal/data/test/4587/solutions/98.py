from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

cnt = 0
for b in B:
    cnt += bisect_left(A, b) * (N - bisect_right(C, b))
print(cnt)
