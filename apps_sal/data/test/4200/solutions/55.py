import decimal
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
base = sum(A) / (4 * M)
for Ai in A:
    if Ai >= base:
        cnt += 1
if cnt >= M:
    print('Yes')
else:
    print('No')
