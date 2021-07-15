n = int(input())
C = [int(a) for a in input().split()]
T = [int(a) for a in input().split()]

CC = [C[i+1]-C[i] for i in range(n-1)]
TT = [T[i+1]-T[i] for i in range(n-1)]

if C[0] == T[0] and C[-1] == T[-1] and sorted(CC) == sorted(TT):
    print("Yes")
else:
    print("No")

