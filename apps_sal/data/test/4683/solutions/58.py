n = int(input())
A = list(map(int, input().split()))

s = 0
sum = 0
ans = 0

for i in range(n):
    s += A[i]

for j in range(n - 1):
    s -= A[j]
    sum += A[j] * s

ans = sum % (10**9 + 7)
print(ans)
