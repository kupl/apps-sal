from collections import deque
import sys
sys.setrecursionlimit(1000000)

S = input()
T = input()
l = len(S)
count = 0
for i in range(l):
    if S[i] != T[i]:
        count += 1

print(count)
