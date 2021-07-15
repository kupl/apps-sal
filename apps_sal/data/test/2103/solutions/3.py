from collections import deque
import sys

N = int(input())

A = [int(_) for _ in input().split()]

jokers = deque()

B = [-1] * N
current = 0


for i, el in enumerate(A):
    jokers.append(i)
    if el != current:
        for j in range(el - current):
            if not jokers:
                print(-1)
                return
            p = jokers.pop()
            if A[p] == current + j:
                print(-1)
                return
            else:
                B[p] = current + j
        current = el

while jokers:
    current += 1
    p = jokers.pop()
    B[p] = current

print(' '.join(map(str, B)))

