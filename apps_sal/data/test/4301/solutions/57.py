import sys

input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))


sort_A = sorted(A, reverse=True)
max_1 = sort_A[0]
max_2 = sort_A[1]

if max_1 == max_2:
    for _ in range(n):
        print(max_1)
else:
    for i in range(n):
        if A[i] == max_1:
            print(max_2)
        else:
            print(max_1)
