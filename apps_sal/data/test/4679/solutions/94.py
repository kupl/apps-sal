import sys
import math
from collections import deque


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

s_at = input()[::-1]
s_bt = input()[::-1]
s_ct = input()[::-1]

s_a = deque()
s_b = deque()
s_c = deque()

for i in range(len(s_at)):
    s_a.append(s_at[i])

for i in range(len(s_bt)):
    s_b.append(s_bt[i])

for i in range(len(s_ct)):
    s_c.append(s_ct[i])

now = "a"

while True:
    if now == "a":
        if len(s_a) == 0:
            print("A")
            return
        now = s_a[-1]
        s_a.pop()
    elif now == "b":
        if len(s_b) == 0:
            print("B")
            return
        now = s_b[-1]
        s_b.pop()
    else:
        if len(s_c) == 0:
            print("C")
            return
        now = s_c[-1]
        s_c.pop()
