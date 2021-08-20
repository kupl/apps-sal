N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
m = min(A, B, C, D, E)
if N % m != 0:
    print(N // m + 5)
else:
    print(N // m + 4)
