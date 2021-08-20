import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
ans = 0
for i in range(N):
    x = bisect.bisect_left(A, B[i])
    y = N - bisect.bisect_right(C, B[i])
    ans += x * y
print(ans)
