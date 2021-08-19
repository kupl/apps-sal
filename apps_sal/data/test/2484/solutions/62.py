import numpy as np
N = int(input())
A = list(map(int, input().split()))
r = 0
temp = 0
ans = 0
for l in range(N):
    while r < N and temp ^ A[r] == temp + A[r]:
        temp += A[r]
        r += 1
    ans += r - l
    if r == l:
        r += 1
        temp = 0
    else:
        temp -= A[l]
print(ans)
