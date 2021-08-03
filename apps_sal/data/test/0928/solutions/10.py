n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

left = 0
ans = 0
sum = 0
for right in range(n):
    sum += A[right]
    while sum >= k:
        sum -= A[left]
        left += 1
    ans += left
print(ans)
