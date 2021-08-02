A, B, K = map(int, input().split())

temp = A
if K >= A:
    K = K - A
    A = 0
else:
    A = A - K
    K = 0

if B >= K:
    B = B - K
else:
    B = 0

print("{} {}".format(A, B))
