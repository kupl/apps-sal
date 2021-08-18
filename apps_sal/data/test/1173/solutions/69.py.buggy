import sys
from collections import deque


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
A = [deque(lr()) for _ in range(N)]
candidate = list(range(N))
match = 0
day = 0

while True:
    day += 1
    used = set()
    next = set()
    bool = False
    for c in candidate:
        if len(A[c]) == 0:
            continue
        op = A[c][0] - 1
        if c in used or op in used:
            continue
        if A[op][0] - 1 == c:
            bool = True
            A[c].popleft()
            A[op].popleft()
            match += 1
            next |= {c, op}
            used |= {c, op}
    if match == N * (N - 1) // 2:
        break
    if not bool:
        print((-1))
        return
    candidate = next

print(day)
