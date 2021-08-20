N = int(input())
A = list(map(int, input().split()))
res = 0
ans = 0
right = 0
for left in range(N):
    while right < N and res ^ A[right] == res + A[right]:
        res += A[right]
        right += 1
    ans += right - left
    if left == right:
        right += 1
    res -= A[left]
print(ans)
