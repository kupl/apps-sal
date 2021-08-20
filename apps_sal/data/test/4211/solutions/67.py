N = int(input())
B = list(map(int, input().split()))
A = B[0] + B[-1]
for i in range(N - 2):
    A += min(B[i], B[i + 1])
print(A)
