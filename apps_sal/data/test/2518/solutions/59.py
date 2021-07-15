import sys
input = sys.stdin.readline

N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]
C = A - B

hi = 10**9 + 1
lo = -1

while hi - lo > 1:
    mid = (hi + lo) // 2
    rem = 0
    for i in range(N):
        rem += max(0, (H[i] - B * mid + C - 1) // C)
    if rem <= mid:
        hi = mid
    else:
        lo = mid

print(hi)
