from collections import deque

S = deque(input())
Q = int(input())

mode = 0
for _ in range(Q):
    T, *FC = input()
    if T == "1":
        mode ^= 1
        continue
    _, F, _, C = FC
    if int(F)+mode == 2: S.append(C)
    else: S.appendleft(C)
print("".join(reversed(S)if mode else S))
