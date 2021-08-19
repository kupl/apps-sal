import re
import copy


def accept_input():
    N = int(input())
    A = {}
    for i in range(1, N + 1):
        A[i] = int(input())
    return N, A


def process(s):
    if s == "#":
        return 1
    else:
        return 0


N, A = accept_input()
cur = 1
kaisu = 0
for _ in range(N):
    cur = A[cur]
    kaisu += 1
    if cur == 2:
        break
if cur == 2:
    print(kaisu)
else:
    print((-1))
