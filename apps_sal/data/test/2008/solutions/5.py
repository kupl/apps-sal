import sys
input = iter(sys.stdin.read().splitlines()).__next__

n = int(input())
A = [[int(x) for x in input().split()] for _ in range(n)]

L = []
R = []

cost = 0
for i in range(n):
    mn = min(A[i])
    cost += mn*(n-1)
    A[i][0] -= mn
    A[i][1] -= mn

    if A[i][0] == 0:
        R.append(A[i][1])
    elif A[i][1] == 0:
        L.append(A[i][0])

cost += sum(i*e for i,e in enumerate(sorted(L, reverse=True)))
cost += sum(i*e for i,e in enumerate(sorted(R, reverse=True)))

print(cost)

