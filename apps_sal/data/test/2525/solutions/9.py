from sys import stdin
from collections import deque


def input():
    return stdin.readline().strip()


S = list(input())
q = deque(S)
is_flipped = False
for _ in range(int(input())):
    q_t, *q_d = input().split()
    if q_t == "1":
        is_flipped = not is_flipped
    else:
        f, c = q_d
        if (not is_flipped and f == "1") or (is_flipped and f == "2"):
            q.appendleft(c)
        else:
            q.append(c)
ans = list(q)
print("".join(ans[::-1])) if is_flipped else print("".join(ans))
