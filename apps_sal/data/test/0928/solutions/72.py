from itertools import accumulate,chain

N,K = map(int,input().split())

A = tuple(map(int,input().split()))
j = 0
s = 0
cnt = 0
for i in range(N):
    while j < N and s < K:
        s += A[j]
        j += 1
    if s < K:
        break
    else:
        cnt += N-j+1
    s -= A[i]

print(cnt)
