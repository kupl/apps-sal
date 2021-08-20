import math
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= i + 1
A.sort()
if N % 2 == 0:
    b = (A[N // 2 - 1] + A[N // 2]) / 2
    bfl = math.floor(b)
    bce = math.ceil(b)
    ansfl = 0
    ansce = 0
    for i in range(N):
        ansfl += abs(A[i] - bfl)
        ansce += abs(A[i] - bce)
    ans = min(ansfl, ansce)
else:
    ans = 0
    b = A[N // 2]
    for i in range(N):
        ans += abs(A[i] - b)
print(ans)
