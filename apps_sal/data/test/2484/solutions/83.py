n = int(input())
A = list(map(int, input().split()))
xsum = A[0]
asum = A[0]
ans = 0
left, right = 0, 0

while True:
    if xsum == asum:
        ans += right - left + 1
        right += 1
        if right == n:
            break
        asum += A[right]
        xsum ^= A[right]
    else:
        asum -= A[left]
        xsum ^= A[left]
        left += 1
print(ans)
