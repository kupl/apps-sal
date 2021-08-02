import sys

n = int(input())
A = list(map(int, sys.stdin.readlines()))

index = 0
past_index = list()
found = False

for i in range(len(A)):
    if index == 1:
        print(i)
        found = True
        break
    index = A[index] - 1

if not found:
    print(-1)
