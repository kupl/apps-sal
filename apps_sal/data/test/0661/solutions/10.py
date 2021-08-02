import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

M, K = lr()

if 2**M <= K or (M == 1 and K == 1):
    print((-1)); return

if K == 0:
    answer = [x // 2 for x in range(2**(M + 1))]

else:
    answer = []
    A = [x for x in range(2**M) if x != K]
    answer.extend(A)
    if K != 0:
        answer.append(K)
    answer.extend(A[::-1])
    if K != 0:
        answer.append(K)

print((*answer))
