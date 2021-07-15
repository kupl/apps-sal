import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, M = lr()
S = list(sr())[::-1]
answer = []
count = 0
cur = 0
while True:
    next = cur
    for i in range(M, 0, -1):
        if cur + i > N:
            continue
        if S[cur+i] == '0':
            count += 1
            next = cur + i
            answer.append(i)
            break
        else:
            continue
    if next == cur:
        print((-1)); return
    cur = next
    if next == N:
        break

answer = answer[::-1]
print((*answer))

