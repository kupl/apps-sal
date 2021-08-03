import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A0 = [a for a in A if a % 2 == 0]
A1 = [a for a in A if a % 2 == 1]
B0 = [a for a in B if a % 2 == 0]
B1 = [a for a in B if a % 2 == 1]

print(min(len(A0), len(B1)) + min(len(A1), len(B0)))
