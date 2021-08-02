n = int(input())
A = list(map(int, input().split()))
B, total = [], 0
for i in range(n):
    B.append(A[i] - i)
B.sort()
if len(B) % 2 == 0:
    b = (B[n // 2 - 1] + B[n // 2]) // 2
else:
    b = B[n // 2]
for i in range(n):
    total += abs(B[i] - b)
print(total)
