(A, B, C) = map(int, input().split())
A -= B
if C - A <= 0:
    print(0)
else:
    print(C - A)
