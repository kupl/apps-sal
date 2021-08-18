import sys

input = sys.stdin.readline
N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))

for i, a in enumerate(sorted(A, reverse=True)):
    if i == 0:
        first = a
    elif i == 1:
        second = a
    else:
        break

for a in A:
    if a == first:
        print(second)
    else:
        print(first)
