import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ans = 0

for b in B:
    a_count = bisect.bisect_left(A, b)
    c_count = N - bisect.bisect_right(C, b)
    ans += a_count * c_count
print(ans)

