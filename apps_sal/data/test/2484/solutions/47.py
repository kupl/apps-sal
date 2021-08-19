N = int(input())
A = list(map(int, input().split()))
ans = 0
sum = 0
right = 0
for left in range(N):
    temp = 0
    while right < N and sum ^ A[right] == sum + A[right]:
        sum = sum ^ A[right]
        right += 1
    if left == right:
        right += 1
    else:
        sum = sum ^ A[left]
    ans += right - left
print(ans)
