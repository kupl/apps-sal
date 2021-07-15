n = int(input())
A = sorted([int(a) for a in input().split()])[::-1]
m = int(input())
Q = [int(a) for a in input().split()]
s = sum(A)
for q in Q:
    print(s-A[q-1])

