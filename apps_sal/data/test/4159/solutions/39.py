(A, B, K) = map(int, input().split())
if K > A:
    K -= A
    A = 0
    B -= K
    B = 0 if B < 0 else B
else:
    A -= K
print(A, B)
