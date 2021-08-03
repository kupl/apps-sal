#min(B, D)-max(A, C)
A, B, C, D = map(int, input().split())
if min(B, D) >= max(A, C):
    print(min(B, D) - max(A, C))
else:
    print(0)
