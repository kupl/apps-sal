n = int(input())
A = list(map(int, input().split()))
b = [0] * n
if n % 2 == 0:
    k = 1
else:
    k = -1
index_ = int(n / 2)
for i in range(n):
    index_ += i * k
    b[index_] = A[i]
    k *= -1
print(*b)
