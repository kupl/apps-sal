H, W = list(map(int, input().split()))
N = int(input())
from collections import deque

A = deque(list(map(int, input().split())))
nuriwake = 1
ans = []
for i in range(H):
    t = []
    for j in range(W):
        if A[0] == 0:
            A.popleft()
            nuriwake += 1
        A[0] -= 1
        t.append(nuriwake)
    if i % 2 != 0:
        t = reversed(t)
    ans.append(t)
for a in ans:
    print((' '.join(map(str, a))))

