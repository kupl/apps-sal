import sys
import copy
from collections import deque


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
A = [deque(lr()) for _ in range(N)]

match = 0
candidate = []
used = set()
for i in range(N):
    bool = False
    if len(A[i]) == 0:
        continue
    op = A[i][0] - 1
    if op in used or i in used:
        continue
    if A[op][0] - 1 == i:
        used.add(i)
        used.add(op)
        candidate.extend([i, op])
        match += 1
        bool = True
        A[i].popleft()
        A[op].popleft()
answer = 1

while True:
    used = set()
    bool = False
    c = []
    for i in candidate:
        if len(A[i]) == 0:
            continue
        op = A[i][0] - 1
        if op in used or i in used:
            continue
        if A[op][0] - 1 == i:
            used.add(i)
            used.add(op)
            match += 1
            c.extend([i, op])
            bool = True
            A[i].popleft()
            A[op].popleft()

    answer += 1
    candidate = c
    if match == N * (N - 1) // 2:
        break
    if not bool:
        print((-1))
        return

print(answer)
