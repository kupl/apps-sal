from bisect import *
N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

cnt = []

for b in B:
    cnt.append(bisect_left(A, b) * (N - bisect_right(C, b)))
print((sum(cnt)))

