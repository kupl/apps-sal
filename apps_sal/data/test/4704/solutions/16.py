from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))

if n == 2:
    print(abs(A[0]-A[1]))
    return

B = list(accumulate(A))

ans = float("inf")
y = 0
for i in range(n-1, 0, -1):
    x = B[i-1]
    y += A[i]
    ans = min(ans, abs(x-y))
print(ans)
