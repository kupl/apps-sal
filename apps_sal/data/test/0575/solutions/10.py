def sign(x):
    return x > 0 - x < 0


n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [B[0] - A[0], B[1] - A[1]]
C = [C[0] - A[0], C[1] - A[1]]

ok = True
if sign(B[0]) != sign(C[0]) or sign(B[1]) != sign(C[1]):
    ok = False

# B = [abs(B[0]), abs(B[1])]
# C = [abs(C[0]), abs(C[1])]

# if B[0] > B[1] and C[0] < C[1]:
#     ok = False
# if B[0] < B[1] and C[0] > C[1]:
#     ok = False

print(["NO", "YES"][ok])
