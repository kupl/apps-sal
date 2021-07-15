N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
import bisect

ans = 0

for i in range(N):
    b = B[i]
    a_idx = bisect.bisect_left(A, b)
    # print(b_idx)
    if a_idx == 0: continue
    c_idx = bisect.bisect_right(C, b)
    c_cnt = N - c_idx
    ans += a_idx * c_cnt
print(ans)

