# ABC140
# Buffet
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ct = 0
h = 25
for i in range(n):
    ct += B[i]
    if h + 1 == A[i]:
        ct += C[h - 1]
        h = A[i]
    else:
        h = A[i]
print(ct)
