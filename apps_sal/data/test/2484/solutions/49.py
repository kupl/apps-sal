N = int(input())
A = list(map(int,input().split()))

right = 0
SUM = 0
ans = 0
for left in range(N):
    while right < N and SUM | A[right] == SUM + A[right]:
        SUM += A[right]
        right += 1
    
    ans += right - left
    
    if right == left:
        right += 1
    else:
        SUM -= A[left]
print(ans)
