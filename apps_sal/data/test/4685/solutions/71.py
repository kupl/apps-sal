A, B, C = map(int, input().split())
K = int(input())
if max(A, B, C) == A:
    A *= 2**K
elif max(A, B, C) == B:
    B *= 2**K
else:
    C *= 2**K
print(A+B+C)
