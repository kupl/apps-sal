from collections import deque
from copy import copy
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
stack = deque()
for i in range(1, N + 1):
    stack.append(([i], set([i])))
a = -1
b = -1
counter = 0
while len(stack) > 0:
    (X, already) = stack.pop()
    if len(X) == N:
        counter += 1
        is_a = True
        is_b = True
        for i in range(N):
            if X[i] != P[i]:
                is_a = False
            if X[i] != Q[i]:
                is_b = False
        if is_a:
            a = counter
        if is_b:
            b = counter
    else:
        for i in range(1, N + 1):
            if i in already:
                continue
            tmp = copy(X)
            tmp.append(i)
            tmp_already = copy(already)
            tmp_already.add(i)
            stack.append((tmp, tmp_already))
    if a != -1 and b != -1:
        break
print(abs(a - b))
