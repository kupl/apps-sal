import math
n = int(input())
A = list(map(int, input().split()))
x1 = 0
for i in range(n):
    x1 += ((-1)**i) * A[i]
arr = [x1]
s = x1 // 2
for i in range(n - 1):
    s = A[i] - s
    arr.append(s * 2)
print((' '.join(map(str, arr))))
