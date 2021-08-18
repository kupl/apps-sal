# coding: utf-8
import sys


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, A, B = lr()
if A + B - 1 > N:
    print((-1))
    return
if A * B < N:
    print((-1))
    return

if B == 1:
    q, r = A, 0
else:
    q, r = divmod(N - A, B - 1)

if q == A:
    size = [B] * q
else:
    size = [B] * q + [r + 1] + [1] * (A - q - 1)

end = 1
answer = []
for s in size:
    start = end + s - 1
    answer.extend(list(range(start, end - 1, -1)))
    end = start + 1

print((*answer))
