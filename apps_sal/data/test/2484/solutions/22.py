N = int(input())
A = list(map(int, input().split()))
left = 0
right = 0
ans = 0
tmp = 0
for left in range(N):
    while right < N and tmp + A[right] == tmp ^ A[right]:
        tmp += A[right]
        right += 1
    ans += right - left
    if right == left:
        right += 1
    else:
        tmp -= A[left]
print(ans)
