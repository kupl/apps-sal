N = int(input())
A = [int(i) for i in input().split()]

left = 0
total = 0
xor = 0
ans = 0
for right in range(N):
    total += A[right]
    xor ^= A[right]
    while total != xor:
        total -= A[left]
        xor ^= A[left]
        left += 1
    ans += right - left + 1
    
print(ans)
