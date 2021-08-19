N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N - K > 0:
    total = K * X + (N - K) * Y
else:
    total = N * X
print(total)
